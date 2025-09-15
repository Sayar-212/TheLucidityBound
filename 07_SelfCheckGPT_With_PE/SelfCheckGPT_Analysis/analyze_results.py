import pandas as pd
import glob

# Find all CSV files
csv_files = glob.glob("selfcheck_*_results_*.csv")

model_hallucination_rates = {}

for file in csv_files:
    df = pd.read_csv(file)
    if 'model' in df.columns and 'passage_score' in df.columns:
        for model in df['model'].unique():
            model_data = df[df['model'] == model]
            # Apply correct threshold logic: scores > 0.5 = hallucination
            has_hallucination = model_data['passage_score'] > 0.5
            hallucination_rate = (has_hallucination.sum() / len(model_data)) * 100
            
            if model not in model_hallucination_rates:
                model_hallucination_rates[model] = []
            model_hallucination_rates[model].append(hallucination_rate)

# Calculate average hallucination rates
print("HALLUCINATION RATES BY MODEL:")
print("="*40)
for model, rates in model_hallucination_rates.items():
    avg_rate = sum(rates) / len(rates)
    print(f"{model}: {avg_rate:.1f}%")

# Find model with least hallucination
if model_hallucination_rates:
    best_model = min(model_hallucination_rates.keys(), 
                    key=lambda x: sum(model_hallucination_rates[x]) / len(model_hallucination_rates[x]))
    best_rate = sum(model_hallucination_rates[best_model]) / len(model_hallucination_rates[best_model])
    print(f"\nLEAST HALLUCINATION: {best_model} ({best_rate:.1f}%)")