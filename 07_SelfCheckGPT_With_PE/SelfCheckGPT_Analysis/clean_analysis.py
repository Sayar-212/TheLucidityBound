import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import glob

# Professional styling
plt.style.use('default')
sns.set_style("whitegrid")
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 11,
    'figure.titlesize': 16,
    'font.family': 'serif'
})

def load_data():
    bertscore_files = glob.glob("selfcheck_bertscore_results_*.csv")
    nli_files = glob.glob("selfcheck_nli_results_*.csv")
    
    bertscore_df = pd.concat([pd.read_csv(f) for f in bertscore_files], ignore_index=True) if bertscore_files else pd.DataFrame()
    nli_df = pd.concat([pd.read_csv(f) for f in nli_files], ignore_index=True) if nli_files else pd.DataFrame()
    
    return bertscore_df, nli_df

def create_figure_1():
    """Method Comparison"""
    bertscore_df, nli_df = load_data()
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Hallucination Detection Method Comparison', fontsize=16, fontweight='bold')
    
    # 1. Detection Rates
    if not bertscore_df.empty and not nli_df.empty:
        methods = ['BERTScore', 'NLI']
        rates = [bertscore_df['has_hallucination'].mean(), nli_df['has_hallucination'].mean()]
        
        bars = ax1.bar(methods, rates, color=['#2E86AB', '#A23B72'], alpha=0.8, edgecolor='black')
        ax1.set_ylabel('Hallucination Detection Rate')
        ax1.set_title('Detection Rate by Method')
        ax1.set_ylim(0, 1)
        
        for bar, rate in zip(bars, rates):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, 
                    f'{rate:.1%}', ha='center', fontweight='bold')
    
    # 2. Score Distributions
    if not bertscore_df.empty:
        ax2.hist(bertscore_df['passage_score'], bins=20, alpha=0.7, label='BERTScore', 
                color='#2E86AB', density=True, edgecolor='black', linewidth=0.5)
    if not nli_df.empty:
        ax2.hist(nli_df['passage_score'], bins=20, alpha=0.7, label='NLI', 
                color='#A23B72', density=True, edgecolor='black', linewidth=0.5)
    ax2.set_xlabel('Passage Score')
    ax2.set_ylabel('Density')
    ax2.set_title('Score Distribution')
    ax2.legend()
    
    # 3. Category Analysis
    combined_df = pd.concat([bertscore_df.assign(method='BERTScore'), 
                            nli_df.assign(method='NLI')], ignore_index=True)
    
    if not combined_df.empty and 'category' in combined_df.columns:
        category_stats = combined_df.groupby('category')['has_hallucination'].mean().sort_values()
        
        bars = ax3.barh(range(len(category_stats)), category_stats.values, 
                       color='#F18F01', alpha=0.8, edgecolor='black')
        ax3.set_yticks(range(len(category_stats)))
        ax3.set_yticklabels(category_stats.index)
        ax3.set_xlabel('Hallucination Rate')
        ax3.set_title('Hallucination by Category')
        
        for i, value in enumerate(category_stats.values):
            ax3.text(value + 0.01, i, f'{value:.1%}', va='center')
    
    # 4. Model Performance
    if not combined_df.empty and 'model' in combined_df.columns:
        model_stats = combined_df.groupby('model').agg({
            'has_hallucination': 'mean',
            'passage_score': 'mean'
        })
        
        ax4.scatter(model_stats['passage_score'], model_stats['has_hallucination'], 
                   s=100, alpha=0.7, color='#C73E1D', edgecolor='black')
        
        for model, row in model_stats.iterrows():
            ax4.annotate(model, (row['passage_score'], row['has_hallucination']),
                        xytext=(5, 5), textcoords='offset points', fontsize=10)
        
        ax4.set_xlabel('Average Passage Score')
        ax4.set_ylabel('Hallucination Rate')
        ax4.set_title('Model Performance')
    
    plt.tight_layout()
    plt.savefig('figure1_method_comparison.png', dpi=300, bbox_inches='tight')
    plt.savefig('figure1_method_comparison.pdf', dpi=300, bbox_inches='tight')
    plt.show()

def create_figure_2():
    """Performance Analysis"""
    bertscore_df, nli_df = load_data()
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Performance Analysis', fontsize=16, fontweight='bold')
    
    # 1. Threshold Analysis
    if not bertscore_df.empty:
        thresholds = np.linspace(0.1, 0.9, 20)
        precision_scores = []
        recall_scores = []
        
        for thresh in thresholds:
            predicted = bertscore_df['passage_score'] > thresh
            actual = bertscore_df['has_hallucination']
            
            tp = ((predicted == True) & (actual == True)).sum()
            fp = ((predicted == True) & (actual == False)).sum()
            fn = ((predicted == False) & (actual == True)).sum()
            
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            
            precision_scores.append(precision)
            recall_scores.append(recall)
        
        ax1.plot(thresholds, precision_scores, 'o-', label='Precision', linewidth=2, color='#2E86AB')
        ax1.plot(thresholds, recall_scores, 's-', label='Recall', linewidth=2, color='#A23B72')
        ax1.set_xlabel('Threshold')
        ax1.set_ylabel('Score')
        ax1.set_title('Precision-Recall vs Threshold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
    
    # 2. Improvement Distribution
    if not bertscore_df.empty and 'improvement' in bertscore_df.columns:
        improvements = bertscore_df['improvement'].dropna()
        
        ax2.hist(improvements, bins=20, alpha=0.8, color='#F18F01', edgecolor='black')
        ax2.axvline(improvements.mean(), color='red', linestyle='--', linewidth=2, 
                   label=f'Mean: {improvements.mean():.3f}')
        ax2.set_xlabel('Improvement Score')
        ax2.set_ylabel('Frequency')
        ax2.set_title('Enhancement Improvement')
        ax2.legend()
    
    # 3. Score Correlation
    if not bertscore_df.empty:
        numeric_cols = ['passage_score', 'has_hallucination', 'threshold_used']
        if 'improvement' in bertscore_df.columns:
            numeric_cols.append('improvement')
        
        corr_data = bertscore_df[numeric_cols].corr()
        
        im = ax3.imshow(corr_data, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
        ax3.set_xticks(range(len(corr_data.columns)))
        ax3.set_yticks(range(len(corr_data.columns)))
        ax3.set_xticklabels(corr_data.columns, rotation=45, ha='right')
        ax3.set_yticklabels(corr_data.columns)
        ax3.set_title('Feature Correlation')
        
        for i in range(len(corr_data.columns)):
            for j in range(len(corr_data.columns)):
                ax3.text(j, i, f'{corr_data.iloc[i, j]:.2f}', 
                        ha='center', va='center', fontweight='bold')
    
    # 4. Enhanced vs Original Scores
    if not bertscore_df.empty and 'enhanced_passage_score' in bertscore_df.columns:
        original = bertscore_df['passage_score']
        enhanced = bertscore_df['enhanced_passage_score']
        
        ax4.scatter(original, enhanced, alpha=0.6, s=30, color='#C73E1D', edgecolor='black')
        
        min_score = min(original.min(), enhanced.min())
        max_score = max(original.max(), enhanced.max())
        ax4.plot([min_score, max_score], [min_score, max_score], 'r--', alpha=0.8, linewidth=2)
        
        ax4.set_xlabel('Original Score')
        ax4.set_ylabel('Enhanced Score')
        ax4.set_title('Original vs Enhanced Scores')
    
    plt.tight_layout()
    plt.savefig('figure2_performance_analysis.png', dpi=300, bbox_inches='tight')
    plt.savefig('figure2_performance_analysis.pdf', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    print("Creating Figure 1: Method Comparison...")
    create_figure_1()
    print("Creating Figure 2: Performance Analysis...")
    create_figure_2()
    print("Analysis complete! Generated publication-ready figures.")