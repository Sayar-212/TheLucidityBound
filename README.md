# **Lucidity-Bound-Framework**  
*A Unified Framework for Hallucination Benchmarking and Mitigation in Large Language Models*  

**Authors:**  
Deblina Chowdhury, Sayar Basu, Piyush Kumar Bharti  
Heritage Institute of Technology, Kolkata  

---

## 📘 Overview  

This repository hosts the official implementation of our research on **hallucination evaluation and mitigation in Large Language Models (LLMs)**. We propose the **Lucidity Bound Framework**, a unified methodology that introduces a **Lucidity Score metric** for standardized benchmarking of hallucinations, while also developing a **defense-in-depth mitigation pipeline**.  

We evaluate our framework on five prominent open-source LLMs — **Gemma 7B, Mistral 7B, LLaMA 3 8B, Qwen 2.5 3B, and DeepSeek-LLM** — across **90 diverse questions spanning multiple knowledge domains**.  

---

## 🚀 Key Contributions  

- **Lucidity Score** → A novel unified metric for hallucination assessment  
- **Cross-Model Evaluation** → Systematic evaluation on **90 domain-diverse queries**  
- **Defense-in-Depth Mitigation** → Combining **RAG, SelfCheckGPT, and Prompt Engineering**  
- **Quantitative Insights** → LLaMA 3 8B achieved the **highest Lucidity Score (62.2)**, outperforming other models statistically  

---

## 📂 Repository Structure  

```
lucidity-bound-framework/
├── paper/                     # Research paper and supplementary materials
├── notebooks/                 
│   ├── evaluation/            # Model evaluation scripts
│   ├── mitigation/            # Hallucination mitigation methods
│   └── analysis/              # Statistical analysis tools
├── data/                      
│   ├── evaluation_questions/  # 90 questions across 6 categories
│   ├── rag_knowledge_base/    # RAG document collection
│   └── results/               # Experimental results
└── requirements.txt           # Dependencies
```

---

## ⚡ Quick Start  

```bash
# Clone the repository
git clone https://github.com/deblina3/lucidity-bound-framework.git
cd lucidity-bound-framework

# Install dependencies
pip install -r requirements.txt
```

---

## 📊 Main Results  

- **LLaMA 3 8B** → Lucidity Score **62.2** (Rank 1)  
- **Mistral 7B** → Lucidity Score **56.9** (Rank 2)  
- **Qwen 2.5 3B** → Lucidity Score **54.7** (Rank 3)  
- **DeepSeek-LLM** → Lucidity Score **53.3** (Rank 4)  
- **Gemma 7B** → Lucidity Score **43.4** (Rank 5)  

---

## 📖 Citation  

```bibtex
@misc{chowdhury2025lucidity,
  title={The Lucidity Bound: A Unified Framework for Hallucination Benchmarking and Mitigation in Large Language Models},
  author={Chowdhury, Deblina and Basu, Sayar and Bharti, Piyush Kumar},
  year={2025},
  note={Under review}
}
```

---

## 📬 Contact  

For questions regarding this research:  
- **Deblina Chowdhury**: deblina.chowdhury@heritageit.edu  
- **Sayar Basu**: sayar.basu.cse26@heritageit.edu.in  

---

## 📜 License  

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  
