#STEP 1
!pip install prophet

import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# --- STEP 2: LOAD & CLEAN DATA ---
print("Loading dataset...")
# Load your specific file
df = pd.read_csv('PDB_dataset.csv')

# Create a proper Datetime column by combining Date and Hour
# This helps us sort the data correctly
df['Datetime'] = pd.to_datetime(df['date']) + pd.to_timedelta(df['hour'] - 1, unit='h')

# Set index to Datetime
df = df.set_index('Datetime')

# Sort data chronologically (Crucial for time series)
df = df.sort_index()

# AGGREGATE: Microsoft cares about Peak Capacity.
# We will take the MAX demand of each day to simulate "Capacity Needed"
daily_peak = df['demand'].resample('D').max().reset_index()

# Rename columns for Prophet (It requires 'ds' and 'y')
daily_peak.columns = ['ds', 'y']

print("Data successfully loaded and aggregated to Daily Peaks!")
print(daily_peak.head())

# --- STEP 3: TRAIN THE MODEL (PROPHET) ---
print("Training the Forecast Model...")
# Initialize Prophet with seasonality enabled
m = Prophet(yearly_seasonality=True, weekly_seasonality=True)

# Train the model
m.fit(daily_peak)

# Create future dates (Forecast 365 days into the future)
future = m.make_future_dataframe(periods=365)

# Predict
forecast = m.predict(future)

# --- STEP 4: CREATE MICROSOFT SCENARIOS ---
print("Creating Scenarios for Power BI...")

# Prepare the export file
results = forecast[['ds', 'yhat']].copy()
results.columns = ['Date', 'Baseline_Forecast']

# Add Historical Data (so we can see the past in the graph)
results = results.merge(daily_peak, left_on='Date', right_on='ds', how='left')
results.rename(columns={'y': 'Historical_Actual'}, inplace=True)
del results['ds'] # Cleanup

# SCENARIO 1: GenAI Boom (High Growth)
# Simulate a 20% surge in demand starting from the last day of actual data
last_actual_date = daily_peak['ds'].max()
results['GenAI_Scenario'] = results['Baseline_Forecast']

# Apply 20% growth only to future dates
future_mask = results['Date'] > last_actual_date
results.loc[future_mask, 'GenAI_Scenario'] = results.loc[future_mask, 'Baseline_Forecast'] * 1.20

# SCENARIO 2: Capacity Threshold (The Risk Line)
# Let's assume the current Data Center Max Capacity is slightly above your highest historical demand
max_historical = daily_peak['y'].max()
capacity_limit = max_historical * 1.05 # 5% buffer above history
results['Max_Capacity_MW'] = capacity_limit

# --- STEP 5: EXPORT ---
output_filename = 'Microsoft_Capacity_Forecast.csv'
results.to_csv(output_filename, index=False)
print(f"SUCCESS! File saved as: {output_filename}")
print("Now open Power BI and import this file.")
