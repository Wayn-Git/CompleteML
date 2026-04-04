# Machine Learning Roadmap

---

## Phase 0 — What is Machine Learning?

> Build the mental model before writing a single line of code.

Machine learning is a way of teaching computers to learn from data rather than following rigid rules you write yourself. Instead of programming every decision, you give the model examples and it figures out the pattern on its own.

**Core concepts to understand first:**
- What is a model?
- What does "training" mean?
- What are inputs and outputs?
- Why data is the fuel of ML

---

## Phase 1 — Foundations

### 1A — Python Basics
Before touching any ML library, get comfortable with Python.

- Variables and data types
- Loops and conditionals
- Functions
- Lists and dictionaries
- File I/O basics

### 1B — Math Essentials
> Refer to the Mathematical_Foundation File 

---

## Phase 2 — Data Tools

> Work with data before you model it.

| Library | Purpose |
|---|---|
| **NumPy** | Arrays, numerical operations, linear algebra |
| **Pandas** | Tables, data cleaning, manipulation |
| **Matplotlib** | Basic plots and charts |
| **Seaborn** | Statistical visualisations |

**Mini project:** Explore a real dataset. Answer questions using only code — no model yet. Practice loading, cleaning, and visualising data end to end.

---

## Phase 3 — Types of Machine Learning

Understand the three paradigms conceptually before jumping into algorithms.

### Supervised Learning
- Data has both **inputs (X)** and **labelled outputs (y)**
- Model learns to map input → output
- **Regression** — predict a number (e.g. house price)
- **Classification** — predict a category (e.g. spam vs. not spam)

### Unsupervised Learning
- Data has **no labels**
- Model finds hidden structure on its own
- **Clustering** — group similar items (e.g. K-Means)
- **Dimensionality reduction** — compress data (e.g. PCA)

### Reinforcement Learning *(later)*
- Model learns by receiving rewards and penalties
- Used in games, robotics, and autonomous systems
- Come back to this after supervised and unsupervised are solid

---

## Phase 4 — Classical ML with Scikit-Learn

### The Standard ML Workflow
Master this loop. Every ML project you ever build follows this exact sequence:

```
1. Load data
2. Clean data
3. Split data  →  Train set + Test set
4. Train model
5. Generate predictions
6. Evaluate results
```

### Algorithms to Learn

**Regression**
- Linear Regression

**Classification**
- Logistic Regression
- K-Nearest Neighbours (KNN)

**Clustering**
- K-Means

### Model Evaluation
- Accuracy
- Precision and Recall
- F1 Score
- Confusion Matrix
- Train/Test Split

**Mini project:** Build a prediction model on a Kaggle dataset end to end. Go through every step of the workflow at least twice.

---

## Phase 5 — Deep Learning

Only move here once classical ML feels comfortable. Pick **one** framework and go deep rather than splitting attention between both.

### Option A — TensorFlow / Keras
- Artificial Neural Networks (ANNs)
- Input and Dense layers
- Activation functions — ReLU, Sigmoid, Softmax
- Loss functions
- Model training and evaluation

### Option B — PyTorch
- Tensors
- The forward pass
- The manual training loop
- Loss functions and optimisers

> **Rule:** Pick one and commit. TensorFlow/Keras has a gentler learning curve. PyTorch is more flexible and widely used in research. Either is a solid choice.

**Mini project:** Build an image classifier.

---

## Phase 6 — Advanced Topics

After the core roadmap is solid, these topics will sharpen your work significantly.

- **Feature Engineering** — transform raw data into better inputs
- **Cross-Validation** — more reliable model evaluation
- **Hyperparameter Tuning** — optimise model performance
- **Statistics** — mean, variance, probability distributions in depth
- **Model Deployment** — Flask, FastAPI, or Gradio

---

## Mistakes to Avoid

- Skipping ML fundamentals before jumping to libraries
- Moving to deep learning before classical ML is solid
- Treating data cleaning as optional (it's often 80% of the work)
- Watching tutorials without building anything yourself
- Bouncing between frameworks without finishing one

---

## Learning Order (Strict)

```
Python Basics
    ↓
Math Essentials
    ↓
NumPy → Pandas → Matplotlib → Seaborn
    ↓
ML Concepts (Supervised / Unsupervised)
    ↓
Scikit-Learn
    ↓
TensorFlow  OR  PyTorch
    ↓
Advanced Topics
```

---
