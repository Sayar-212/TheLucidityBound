# lucidity-bound-framework
A Unified Framework for Hallucination Benchmarking and Mitigation in Large Language Models
# The Lucidity Bound: A Unified Framework for Hallucination Benchmarking and Mitigation in Large Language Models

**Authors:** Deblina Chowdhury, Sayar Basu, Piyush Kumar Bharti  
Heritage Institute of Technology, Kolkata

## About

This repository contains the implementation of our research on evaluating and mitigating hallucinations in Large Language Models. We introduce the Lucidity Bound framework and evaluate five open-source models: Gemma 7B, Mistral 7B, LLaMA 3 8B, Qwen 2.5 3B, and DeepSeek-LLM.

## Key Contributions

- Lucidity Score metric for unified hallucination assessment
- Comprehensive evaluation across 90 questions in multiple domains
- Defense-in-depth mitigation framework (RAG + SelfCheckGPT + Prompt Engineering)
- Statistical analysis showing LLaMA 3 8B achieved highest Lucidity Score (62.2)

## Repository Structure
```
├── paper/                     # Research paper and supplementary materials
├── notebooks/                # Jupyter notebooks
│   ├── evaluation/           # Model evaluation scripts
│   ├── mitigation/           # Hallucination mitigation methods
│   └── analysis/             # Statistical analysis tools
├── data/                      # Evaluation questions and results
│   ├── evaluation_questions/ # 90 questions across 6 categories
│   ├── rag_knowledge_base/   # RAG document collection
│   └── results/              # Experimental results
└── requirements.txt          # Dependencies
```
## Quick Start

# Clone repository
git clone https://github.com/deblina3/lucidity-bound-framework.git
cd lucidity-bound-framework

# Install dependencies
pip install -r requirements.txt

## Main Results

- LLaMA 3 8B: Lucidity Score 62.2 (Rank 1)
- Mistral 7B: Lucidity Score 56.9 (Rank 2)  
- Qwen 2.5 3B: Lucidity Score 54.7 (Rank 3)
- DeepSeek-LLM: Lucidity Score 53.3 (Rank 4)
- Gemma 7B: Lucidity Score 43.4 (Rank 5)

## Citation

@misc{chowdhury2025lucidity,
  title={The Lucidity Bound: A Unified Framework for Hallucination Benchmarking and Mitigation in Large Language Models},
  author={Chowdhury, Deblina and Basu, Sayar and Bharti, Piyush Kumar},
  year={2025},
  note={Under review}
}

## Contact

For questions about this research:
- Deblina Chowdhury: deblina.chowdhury@heritageit.edu
- Sayar Basu: sayar.basu.cse26@heritageit.edu.in

## License

MIT License - see LICENSE file for details.
