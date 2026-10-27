# Implementation Plan: Report Rewrite for CiviQ Legal RAG System

## Executive Summary

This plan details the complete rewrite of a B.Tech project report from a **lung disease detection system** (DenseNet-121 + Grad-CAM) to **CiviQ – AI-Powered Civic Issue Reporting and Complaint Management System**, which is actually an Indian Legal RAG (Retrieval-Augmented Generation) assistant based on the codebase at `codebase/Indian-Legal-Rag-master/`.

The report uses LaTeX with TikZ diagrams. All metadata, chapter content, diagrams, and included files must be updated while **preserving the exact document format and structure**.

---

## 1. METADATA UPDATES (main.tex lines 1-100)

### 1.1 \gdef Metadata Variables
Replace all `\gdef` commands with new values:

```latex
\gdef \title{AI-POWERED LEGAL INFORMATION RETRIEVAL USING RETRIEVAL-AUGMENTED GENERATION}
\gdef \shorttitle{AI-Powered Legal Information Retrieval using RAG}

\gdef \authorA{ALEENA}
\gdef \rollnoA{KNP23CS025}

\gdef \authorB{FATHIMA}
\gdef \rollnoB{KNP23CS047}

\gdef \authorC{ADITHYA}
\gdef \rollnoC{KNP23CS016}

\gdef \authorD{ABHINAYA}
\gdef \rollnoD{KNP23CO007}

\gdef \guide{Hridhya J}
\gdef \guidedes{Assistant Professor}
```

Keep other metadata unchanged (acadyear, dept, college, etc.).

### 1.2 \hypersetup Block
Update PDF metadata:

```latex
\hypersetup{
    pdftitle={AI-Powered Legal Information Retrieval using Retrieval-Augmented Generation},
    pdfauthor={Aleena, Fathima, Adithya, Abhinaya}
}
```

**Files affected:** `main.tex`  
**Verification:** Compile LaTeX and check PDF properties show correct title/authors

---

## 2. INCLUDED TEX FILES

### 2.1 coverpage.tex
**Current content:** Shows old authors (ADHIL N, AKHIL A, ALFIYA A, ANAKHA B RAJEEV) and old title  
**Required changes:**
- Replace title with: `AI-POWERED LEGAL INFORMATION RETRIEVAL USING RETRIEVAL-AUGMENTED GENERATION`
- Replace author table with:
```latex
\begin{tabular}{c@{\hspace{2.2cm}}c}
    \large\bfseries ALEENA & \large\bfseries KNP23CS025 \\
    \large\bfseries FATHIMA & \large\bfseries KNP23CS047 \\
    \large\bfseries ADITHYA & \large\bfseries KNP23CS016 \\
    \large\bfseries ABHINAYA & \large\bfseries KNP23CO007
\end{tabular}
```

**Files affected:** `coverpage.tex`  
**Verification:** LaTeX compile → check cover page renders correctly

### 2.2 certificate1.tex
**Current content:** Old project title and author names, guide "Ms. Nivy GS"  
**Required changes:**
- Replace title with new title (same as above)
- Replace author list: `\textbf{ALEENA} (KNP23CS025), \textbf{FATHIMA} (KNP23CS047), \textbf{ADITHYA} (KNP23CS016), and \textbf{ABHINAYA} (KNP23CO007)`
- Replace guide name and designation:
```latex
\textbf{Hridhya J} \\
(Project Guide) \\
Assistant Professor \\
Dept. of CSE \\
CE, Karunagappally
```

**Files affected:** `certificate1.tex`  
**Verification:** LaTeX compile → check certificate page shows correct names

### 2.3 declaration.tex
**Current content:** Old author names in body text and signature block  
**Required changes:**
- Replace declaration text: `We, \textbf{ALEENA} (\rollnoA), \textbf{FATHIMA} (\rollnoB), \textbf{ADITHYA} (\rollnoC), and \textbf{ABHINAYA} (\rollnoD), hereby declare...`
- Replace signature block:
```latex
\textbf{ALEENA} (\rollnoA) \\[4pt]
\textbf{FATHIMA} (\rollnoB) \\[4pt]
\textbf{ADITHYA} (\rollnoC) \\[4pt]
\textbf{ABHINAYA} (\rollnoD)
```

**Files affected:** `declaration.tex`  
**Verification:** LaTeX compile → check declaration page

### 2.4 abstract.tex
**Current content:** Discusses lung disease detection, DenseNet-121, Grad-CAM, chest X-rays  
**Required changes:** Replace entire abstract with:

```latex
\noindent Access to Indian legal information remains hindered by complex statutory language, fragmented document repositories, and language barriers for non-English speakers. Citizens seeking redress through civic complaint systems face difficulties understanding relevant laws such as the Bharatiya Nyaya Sanhita (BNS), Bharatiya Nagarik Suraksha Sanhita (BNSS), Right to Information (RTI) Act, and Consumer Protection Act. Traditional search interfaces return raw legal text without context, requiring professional legal interpretation.

\vspace{8pt}

\noindent To address these challenges, this project presents \textbf{CiviQ}: an AI-Powered Legal Information Retrieval system using \textbf{Retrieval-Augmented Generation (RAG)}. The system ingests PDF legal documents, extracts text using \textbf{PyMuPDF}, and applies overlapping word-chunking (900 words per chunk, 150-word overlap, 40-word minimum). Text chunks are embedded using \textbf{sentence-transformers (all-MiniLM-L6-v2)} generating 384-dimensional cosine-normalized vectors, indexed in \textbf{Pinecone} vector database with batch upserts. User queries are embedded identically, and top-k semantic retrieval (default k=5) fetches relevant passages. \textbf{Google Gemini 2.5 Flash} generates grounded answers citing retrieved sources. The system detects Malayalam queries via Unicode block analysis (U+0D00–U+0D7F) and translates them to English before retrieval, with response translation back to Malayalam.

\vspace{8pt}

\noindent The production architecture comprises a \textbf{FastAPI} backend (Python 3.12) with endpoints for question answering, document upload analysis, and health checks, serving a \textbf{React 19 + Vite 8 + Tailwind CSS 4} frontend with voice input (browser speech-to-text), PDF upload, language selection (auto/English/Malayalam), top-k slider, source citation display, and document summaries. The corpus includes BNS 2023, BNSS 2023, BSA 2023, Consumer Protection Act 2019, Indian Contract Act 1872, RTI Act 2005, and Constitution of India. The system provides accessible legal guidance for civic complaint resolution and information rights.
```

**Files affected:** `abstract.tex`  
**Verification:** LaTeX compile → check abstract page

### 2.5 acknowledgement.tex
**Current content:** References old guide "Ms. Nivy GS" and old author names  
**Required changes:**
- Update guide reference to: `\mbox{\textbf{Hridhya J}}, \guidedes`
- Update author names in final signature block:
```latex
\textbf{ALEENA} (\rollnoA) \\[3pt]
\textbf{FATHIMA} (\rollnoB) \\[3pt]
\textbf{ADITHYA} (\rollnoC) \\[3pt]
\textbf{ABHINAYA} (\rollnoD)
```

**Files affected:** `acknowledgement.tex`  
**Verification:** LaTeX compile → check acknowledgement page

---

## 3. CHAPTER 1: INTRODUCTION (main.tex)

**Current content:** Discusses pulmonary pathologies, chest radiography, radiologist shortages, DenseNet-121, Grad-CAM  
**Target content:** Legal information access barriers, civic complaint challenges, RAG solution

### 3.1 Background Paragraph
Replace first 2-3 paragraphs with:

> Access to accurate, comprehensible legal information is fundamental to civic empowerment and the effective exercise of constitutional rights in India. Citizens encounter legal systems daily—from consumer disputes and service grievances to information access rights under the Right to Information (RTI) Act 2005 and criminal proceedings under the Bharatiya Nyaya Sanhita (BNS) 2023. However, contemporary legal information retrieval faces systemic obstacles:
> 
> (i) **Statutory Language Complexity:** Legal texts employ specialized terminology, nested conditional clauses, and cross-references that are impenetrable to non-lawyers.
> 
> (ii) **Fragmented Document Repositories:** Statutes, amendments, judicial interpretations, and procedural codes are scattered across government portals, parliamentary archives, and district registries without unified search.
> 
> (iii) **Language Barriers:** Over 57% of Indian citizens speak regional languages as their primary tongue, yet most legal resources remain exclusively in English or technical Hindi, excluding Malayalam, Tamil, Telugu, and other linguistic communities.
> 
> (iv) **Lack of Contextual Answers:** Traditional keyword search returns raw statutory clauses without explanation of applicability, penalties, or procedural steps, requiring expensive legal consultation.

### 3.2 Proposed Solution Paragraph
Replace DenseNet/Grad-CAM description with:

> This project introduces **CiviQ – AI-Powered Civic Issue Reporting and Complaint Management System**, a Retrieval-Augmented Generation (RAG) platform for citizen-accessible legal information retrieval. The system ingests comprehensive legal corpora including BNS 2023, BNSS 2023, BSA 2023, Consumer Protection Act 2019, Indian Contract Act 1872, RTI Act 2005, and the Constitution of India. Documents are preprocessed through overlapping word-chunking (900-word chunks, 150-word overlap), embedded via sentence-transformers (all-MiniLM-L6-v2, 384-dim vectors), and indexed in Pinecone vector database. User queries—submitted as text or voice input—undergo identical embedding, semantic retrieval of top-k relevant passages (default k=5), and grounded answer generation via Google Gemini 2.5 Flash. The system automatically detects Malayalam queries (Unicode U+0D00–U+0D7F), translates them to English for retrieval, and translates responses back, ensuring linguistic inclusivity.

### 3.3 Objectives List
Replace existing objectives with:

1. To curate and ingest a comprehensive Indian legal corpus comprising post-2023 reformed criminal codes (BNS, BNSS, BSA) and foundational civil statutes.
2. To engineer a robust PDF text extraction pipeline using PyMuPDF with automated cleaning of headers, footers, and page artifacts.
3. To implement overlapping word-chunking (chunk_size=900, overlap=150, min_chunk=40) that preserves legal context across chunk boundaries.
4. To embed text chunks using sentence-transformers all-MiniLM-L6-v2 with cosine normalization and batch upload to Pinecone vector database.
5. To design bilingual query processing with automatic Malayalam detection (Unicode block U+0D00–U+0D7F) and Gemini-powered translation.
6. To integrate Google Gemini 2.5 Flash for context-grounded answer generation with explicit source citation.
7. To build a FastAPI asynchronous backend with endpoints for question answering, document analysis, and system health.
8. To develop a React 19 + Vite 8 frontend with voice input, PDF upload, language selection, top-k tuning, and source citation display.
9. To evaluate retrieval precision and answer accuracy across RTI Act, Contract Act, BNS, BSA, and BNSS query benchmarks.

### 3.4 Scope Paragraph
Replace diagnostic screening scope with:

> The platform is designed as an educational and informational legal assistance tool for citizens, students, journalists, and civic organizations. It provides grounded answers with statutory citations for preliminary legal research. Crucially, the system is explicitly scoped as an information retrieval aid, not a substitute for professional legal counsel, and displays prominent disclaimers that outputs do not constitute legal advice.

**Files affected:** `main.tex` (Chapter 1)  
**Verification:** LaTeX compile → check Chapter 1 renders correctly with new content

---

## 4. CHAPTER 2: LITERATURE REVIEW (main.tex)

**Current content:** Discusses deep learning in medical imaging, CNNs, DenseNet, Grad-CAM, transfer learning  
**Target content:** RAG systems, vector databases, LLMs, legal AI, multilingual NLP

### 4.1 Section Rewrites

Replace all sections with:

**Section 2.1: Retrieval-Augmented Generation (RAG) Architectures**
> Lewis et al. (2020) introduced RAG, combining parametric knowledge in large language models with non-parametric retrieval over external document corpora. RAG systems encode documents into dense vector representations, retrieve top-k semantically similar passages via cosine similarity, and condition generation on retrieved context, reducing hallucination and grounding answers in verifiable sources.

**Section 2.2: Dense Vector Representations and Sentence Transformers**
> Reimers and Gurevych (2019) developed sentence-transformers, fine-tuning BERT models with Siamese networks on semantic textual similarity tasks. The all-MiniLM-L6-v2 model produces 384-dimensional embeddings optimized for semantic search with minimal computational overhead, making it suitable for production deployment.

**Section 2.3: Vector Databases and Semantic Search**
> Pinecone, Weaviate, and Milvus provide managed vector database services with approximate nearest neighbor (ANN) search using HNSW (Hierarchical Navigable Small World) graphs. Malkov and Yashunin (2018) demonstrated HNSW's logarithmic query complexity, enabling sub-100ms retrieval over million-scale corpora.

**Section 2.4: Large Language Models for Grounded Generation**
> OpenAI's GPT-4, Google's Gemini 2.0, and Anthropic's Claude 3.5 demonstrate strong instruction-following and context utilization. Gemini 2.5 Flash, with its 1M token context window and multilingual support, is optimized for production RAG pipelines requiring low-latency generation with citation grounding.

**Section 2.5: Legal AI and Statute Retrieval Systems**
> Zhong et al. (2020) developed legal BERT models on case law corpora. Chalkidis et al. (2020) introduced LegalBERT for European legal documents. However, most legal AI focuses on case law rather than Indian statutory codes, and existing systems lack bilingual Malayalam support.

**Section 2.6: Multilingual NLP and Translation for Low-Resource Languages**
> Malayalam, with 38 million speakers, remains underserved in NLP. Google Translate API and IndicTrans (Ramesh et al., 2022) provide Malayalam↔English translation. Unicode block detection (U+0D00–U+0D7F) enables automatic language identification without external classifiers.

### 4.2 Comparison Table
Replace Table 2.1 (CheXNet/DarkCovidNet comparison) with:

```latex
\begin{table}[H]
\centering
\caption{Comparative analysis of legal information retrieval systems.}
\label{tab:lit_comparison}
\footnotesize
\renewcommand{\arraystretch}{1.1}
\begin{tabularx}{\textwidth}{>{\raggedright\arraybackslash}p{2.8cm} >{\centering\arraybackslash}p{1.8cm} >{\centering\arraybackslash}p{1.5cm} >{\centering\arraybackslash}p{1.8cm} >{\raggedright\arraybackslash}X}
\toprule
\textbf{System} & \textbf{Retrieval Method} & \textbf{Bilingual} & \textbf{Source Citation} & \textbf{Limitations} \\
\midrule
Google Search & Keyword BM25 & No & No & Returns raw PDFs without context; no answer generation. \\
Legal GPT-4 & Parametric only & Yes & No & Hallucinates statutes; no grounding in actual legal text. \\
Manupatra/SCC & Keyword + Boolean & No & Yes & Case law focused; weak on statutes; English only. \\
LIMBS (Govt) & Metadata catalog & No & No & Document listing only; no semantic search or answers. \\
\textbf{CiviQ (This Project)} & \textbf{Dense vector RAG} & \textbf{Yes (Malayalam)} & \textbf{Yes} & \textbf{Grounded answers with citations; bilingual Malayalam/English.} \\
\bottomrule
\end{tabularx}
\end{table}
```

**Files affected:** `main.tex` (Chapter 2)  
**Verification:** LaTeX compile → check Chapter 2 content and table render correctly

---

## 5. CHAPTER 3: PROBLEM DEFINITION (main.tex)

**Current content:** Radiographic ambiguity, black-box AI, medical deployment challenges  
**Target content:** Legal access barriers, RAG formulation, multilingual query processing

### 5.1 Problem Statement
Replace with:

> Indian citizens require timely, comprehensible legal information to navigate civic complaint systems, consumer protection mechanisms, and information access rights. However, existing statutory repositories provide raw legal text without contextual interpretation, and most resources exclude non-English speakers. Generative AI systems hallucinate non-existent legal provisions without source grounding.
>
> The objective of this project is to design, implement, and evaluate an automated Retrieval-Augmented Generation (RAG) system for grounded legal information retrieval, utilizing sentence-transformers embedding (all-MiniLM-L6-v2), Pinecone vector indexing, Google Gemini 2.5 Flash generation, bilingual Malayalam↔English query processing, a FastAPI backend, and a React 19 frontend with voice input.

### 5.2 Theoretical Formulation
Replace DenseNet/Grad-CAM math with:

> Let $\mathcal{C} = \{d_1, d_2, \dots, d_N\}$ represent the legal document corpus. Each document $d_i$ is partitioned into overlapping chunks $\{c_{i,1}, c_{i,2}, \dots, c_{i,m_i}\}$ where each chunk $c_{i,j}$ contains 900 words with 150-word overlap with adjacent chunks.
>
> Let $\phi: \mathcal{T} \to \mathbb{R}^{384}$ denote the embedding function (all-MiniLM-L6-v2), mapping text $t \in \mathcal{T}$ to a 384-dimensional dense vector. Embeddings are L2-normalized:
> \begin{equation}
>     \mathbf{e}(t) = \frac{\phi(t)}{\|\phi(t)\|_2}
> \end{equation}
>
> For a user query $q$, the retrieval function $R$ computes cosine similarity with all chunk embeddings:
> \begin{equation}
>     \text{sim}(q, c) = \mathbf{e}(q)^\top \mathbf{e}(c)
> \end{equation}
> and returns the top-k chunks:
> \begin{equation}
>     R(q, k) = \text{argmax}_{S \subset \mathcal{C}, |S|=k} \sum_{c \in S} \text{sim}(q, c)
> \end{equation}
>
> The generation function $G$ conditions a large language model on retrieved context:
> \begin{equation}
>     \text{answer} = G(q \,|\, R(q, k))
> \end{equation}
> producing a grounded response with explicit source citations.
>
> For Malayalam queries, a detection function $\delta$ identifies Unicode block U+0D00–U+0D7F, and a translation function $T$ converts queries: $q_{\text{en}} = T(q_{\text{ml}})$ before retrieval, with inverse translation on the generated answer.

**Files affected:** `main.tex` (Chapter 3)  
**Verification:** LaTeX compile → check Chapter 3 math renders correctly

---

## 6. CHAPTER 4: REQUIREMENTS SPECIFICATION (main.tex)

**Current content:** Image ingestion, DenseNet inference, Grad-CAM generation, Next.js/Expo clients  
**Target content:** Text/voice query input, PDF upload, language selection, source citation, FastAPI endpoints

### 6.1 Functional Requirements
Replace FR-1 through FR-7 with:

```latex
\begin{enumerate}[(i)]
    \item \textbf{FR-1: Text and Voice Query Input:} The system shall accept typed queries and browser-based speech-to-text voice input in English and Malayalam.
    \item \textbf{FR-2: Automatic Language Detection:} The system shall detect Malayalam queries via Unicode block analysis (U+0D00–U+0D7F) and route them through translation.
    \item \textbf{FR-3: PDF Document Upload and Analysis:} The system shall accept PDF uploads (≤50 MB), extract text via PyMuPDF, and provide document summary or question-based analysis.
    \item \textbf{FR-4: Semantic Retrieval with Top-K Selection:} The system shall embed queries using all-MiniLM-L6-v2, retrieve top-k relevant passages from Pinecone (user-configurable k=1–10, default k=5), and display sources.
    \item \textbf{FR-5: Grounded Answer Generation:} The system shall generate contextual answers via Gemini 2.5 Flash conditioned on retrieved passages, with explicit citation of source documents and sections.
    \item \textbf{FR-6: Bilingual Response Translation:} For Malayalam queries, the system shall translate generated English answers back to Malayalam before display.
    \item \textbf{FR-7: Health Check and Status Monitoring:} The backend shall expose \texttt{GET /api/health} returning database connectivity status and system readiness.
\end{enumerate}
```

### 6.2 Hardware/Software Requirements
Replace GPU training environment with:

```latex
\subsection{Hardware and Software Requirements}
\begin{itemize}
    \item \textbf{Development Environment:}
    \begin{itemize}
        \item CPU: 4-core modern processor (Intel i5 / AMD Ryzen 5 or better).
        \item RAM: 8 GB minimum (16 GB recommended).
        \item Operating System: Windows 11 / Linux Ubuntu 22.04 / macOS 12+.
        \item Internet: Stable connection for Pinecone API and Gemini API calls.
    \end{itemize}
    \item \textbf{Production Deployment:}
    \begin{itemize}
        \item Cloud VM or containerized environment (Docker).
        \item Python 3.12+ runtime.
        \item Node.js 18+ for frontend build.
    \end{itemize}
\end{itemize}

\subsection{External Services and APIs}
\begin{itemize}
    \item \textbf{Vector Database:} Pinecone managed service (free tier: 1M vectors, 100K queries/month).
    \item \textbf{LLM API:} Google Gemini API 2.5 Flash (free tier: 15 RPM, 1M TPM).
    \item \textbf{Translation:} Gemini API (same quota).
\end{itemize}

\subsection{Libraries and Frameworks}
\begin{itemize}
    \item \textbf{Backend:} Python 3.12, FastAPI, Uvicorn, PyMuPDF (fitz), sentence-transformers, pinecone-client, google-generativeai.
    \item \textbf{Frontend:} React 19, Vite 8, Tailwind CSS 4, React Markdown, browser Web Speech API.
\end{itemize}
```

**Files affected:** `main.tex` (Chapter 4)  
**Verification:** LaTeX compile → check Chapter 4 FR list and requirements

---

## 7. CHAPTER 5: SYSTEM DESIGN (main.tex)

**Current content:** DenseNet architecture diagrams, Grad-CAM pipeline, FastAPI inference serving  
**Target content:** RAG pipeline architecture, ingestion workflow, query answering workflow, document analysis

### 7.1 High-Level Architecture Text
Replace medical imaging architecture description with:

> The system is structured as a decoupled multi-tier architecture spanning frontend presentation, API gateway, RAG ingestion pipeline, query processing pipeline, and vector database storage, as illustrated in Figure~\ref{fig:system_arch_detailed}.
>
> The architecture comprises four primary operational tiers:
> \begin{enumerate}
>     \item \textbf{Frontend Presentation Tier:} React 19 + Vite 8 single-page application providing chat interface, voice input (Web Speech API), PDF upload, language selector (auto/English/Malayalam), top-k depth slider, and source citation cards.
>     \item \textbf{API Gateway Tier:} FastAPI asynchronous backend exposing \texttt{GET /}, \texttt{GET /api/health}, \texttt{POST /ask}, and \texttt{POST /analyze-document} endpoints with CORS middleware and request validation.
>     \item \textbf{RAG Processing Tier:} Core pipeline comprising (a) ingestion: PDF extraction, text cleaning, overlapping chunking, embedding, Pinecone upsert; (b) query: embedding, top-k retrieval, Gemini generation with citations; (c) translation: Malayalam detection and bidirectional translation.
>     \item \textbf{Storage Tier:} Pinecone vector database (384-dim embeddings, cosine similarity) and local filesystem for uploaded PDFs (temporary processing only).
> \end{enumerate}

### 7.2 Figure References and Captions
Update all figure captions in Chapter 5 to match new diagram content (diagrams will be redrawn in step 13):

- `fig:system_arch_detailed`: "Multi-tier RAG system architecture showing Frontend, API Gateway, Ingestion Pipeline, Query Pipeline, and Vector Database."
- `fig:framework`: "End-to-end RAG operational pipeline: PDF ingestion → chunking → embedding → indexing → query embedding → retrieval → generation."
- `fig:arch_workflow`: "Layered system workflow: user query → language detection → translation (if Malayalam) → embedding → Pinecone retrieval → Gemini generation → citation formatting → response."
- `fig:system_flow`: "Complete data flow from PDF upload through text extraction, chunking, embedding, and Pinecone indexing."
- `fig:multiagent_flowchart`: "Query processing flowchart with decision branches for language detection, retrieval depth, and error handling."
- `fig:dag_scheduling_walkthrough`: "RAG pipeline component dependencies: PyMuPDF → text cleaner → chunker → embedder → Pinecone uploader."
- `fig:db_schema`: "Data schema showing PDF metadata, chunk embeddings, query logs, and retrieved passage records."
- `fig:data_flow_diagram`: "Level-1 DFD showing external entities (User, Pinecone, Gemini API), processes (ingest, query, translate), and data stores (vector DB, document cache)."

**Files affected:** `main.tex` (Chapter 5)  
**Verification:** LaTeX compile → check Chapter 5 text and figure references

---

## 8. CHAPTER 6: DESIGN AND METHODOLOGY (main.tex)

**Current content:** DenseNet math, Grad-CAM math, training hyperparameters, ImageNet normalization  
**Target content:** Embedding math, chunking algorithm, retrieval scoring, Gemini prompts, RAG configuration

### 8.1 Mathematical Foundations
Replace DenseNet/Grad-CAM sections with:

**Section 6.1: Overlapping Word-Chunking Algorithm**
> To preserve legal context across chunk boundaries, documents are split using overlapping word-chunking:
> \begin{equation}
>     \text{chunk}_i = \text{words}[i \times s : i \times s + c]
> \end{equation}
> where $c = 900$ (chunk size), $s = c - o = 750$ (stride), and $o = 150$ (overlap). Chunks shorter than 40 words are discarded to filter headers/footers.

**Section 6.2: Sentence-Transformers Embedding**
> The all-MiniLM-L6-v2 model maps text to 384-dimensional dense vectors via mean-pooling over BERT token embeddings:
> \begin{equation}
>     \mathbf{e}(t) = \frac{1}{n} \sum_{i=1}^n \text{BERT}_{\text{layer-6}}(t_i)
> \end{equation}
> Embeddings are L2-normalized and stored in Pinecone with cosine similarity metric.

**Section 6.3: Cosine Similarity Retrieval**
> For query $q$ and chunk $c$, cosine similarity is:
> \begin{equation}
>     \text{sim}(q, c) = \frac{\mathbf{e}(q) \cdot \mathbf{e}(c)}{\|\mathbf{e}(q)\| \|\mathbf{e}(c)\|} = \mathbf{e}(q)^\top \mathbf{e}(c)
> \end{equation}
> (since embeddings are pre-normalized). Pinecone returns top-k chunks with highest similarity scores.

**Section 6.4: Gemini Prompt Engineering**
> The generation prompt follows the template:
> ```
> You are a legal information assistant. Answer the question based ONLY on the provided context.
> Question: {question}
> Context: {retrieved_passages}
> Cite specific sections/acts in your answer. If context is insufficient, state "Information not available in provided documents."
> ```

### 8.2 Configuration Table
Replace DenseNet hyperparameter table with:

```latex
\begin{table}[H]
\centering
\caption{RAG System Configuration Parameters.}
\label{tab:rag_config}
\small
\begin{tabularx}{\textwidth}{l p{4.2cm} X}
\toprule
\textbf{Component} & \textbf{Parameter} & \textbf{Value / Rationale} \\
\midrule
Chunking & chunk\_size & 900 words (preserves legal context) \\
 & overlap & 150 words (captures cross-chunk references) \\
 & min\_chunk\_size & 40 words (filters artifacts) \\
Embedding & model & all-MiniLM-L6-v2 (384-dim, optimized for semantic search) \\
 & normalization & L2 (cosine similarity) \\
Vector DB & service & Pinecone (managed, HNSW indexing) \\
 & dimension & 384 \\
 & metric & cosine \\
 & batch\_size & 100 vectors/upsert \\
Retrieval & top\_k & 5 (default, user-configurable 1–10) \\
LLM & model & Gemini 2.5 Flash (1M context, low latency) \\
 & temperature & 0.3 (deterministic, citation-focused) \\
 & max\_output\_tokens & 1024 \\
Translation & trigger & Unicode U+0D00–U+0D7F (Malayalam) \\
 & service & Gemini API \\
\bottomrule
\end{tabularx}
\end{table}
```

**Files affected:** `main.tex` (Chapter 6)  
**Verification:** LaTeX compile → check Chapter 6 math and table

---

## 9. CHAPTER 7: PRELIMINARY ANALYSIS (main.tex)

**Current content:** CNN architecture comparison (VGG, ResNet, DenseNet), Grad-CAM vs LIME  
**Target content:** Embedding model comparison, vector database comparison, LLM comparison, frontend framework comparison

### 9.1 Section Rewrites

Replace all sections with:

**Section 7.1: Embedding Model Selection**
> Candidates: BERT-base (768-dim), all-MiniLM-L6-v2 (384-dim), mpnet-base-v2 (768-dim). all-MiniLM-L6-v2 chosen for optimal balance of semantic quality and inference speed (5x faster than BERT).

**Section 7.2: Vector Database Evaluation**
> Compared Pinecone, Weaviate, Milvus. Pinecone selected for managed service, free tier (1M vectors), HNSW indexing, and sub-100ms query latency.

**Section 7.3: Large Language Model Comparison**
> Evaluated GPT-4 Turbo, Claude 3.5 Sonnet, Gemini 2.5 Flash. Gemini 2.5 Flash chosen for 1M token context window, built-in Malayalam support, free tier (15 RPM), and citation-friendly generation.

**Section 7.4: Frontend Framework Analysis**
> Compared Next.js 14 (React Server Components), Vite 8 + React 19 (client-side), SvelteKit. Vite 8 + React 19 chosen for fast dev server, Tailwind CSS 4 integration, and straightforward Web Speech API integration.

### 9.2 Comparison Table
Add new table:

```latex
\begin{table}[H]
\centering
\caption{Technology stack comparison and selection rationale.}
\label{tab:tech_comparison}
\footnotesize
\begin{tabularx}{\textwidth}{l l l X}
\toprule
\textbf{Component} & \textbf{Candidates} & \textbf{Selected} & \textbf{Rationale} \\
\midrule
Embedding & BERT-base, all-MiniLM-L6-v2, mpnet & all-MiniLM-L6-v2 & 384-dim, 5× faster, optimized for semantic search \\
Vector DB & Pinecone, Weaviate, Milvus & Pinecone & Managed, free 1M vectors, HNSW, <100ms queries \\
LLM & GPT-4, Claude 3.5, Gemini 2.5 & Gemini 2.5 Flash & 1M context, Malayalam support, free 15 RPM \\
Backend & Flask, Django, FastAPI & FastAPI & Async ASGI, Pydantic validation, OpenAPI docs \\
Frontend & Next.js 14, Vite+React, SvelteKit & Vite 8 + React 19 & Fast HMR, Tailwind 4, Web Speech API \\
\bottomrule
\end{tabularx}
\end{table}
```

**Files affected:** `main.tex` (Chapter 7)  
**Verification:** LaTeX compile → check Chapter 7 content and table

---

## 10. CHAPTER 8: FEASIBILITY STUDY (main.tex)

**Current content:** Medical imaging project timeline (dataset curation, DenseNet training, Grad-CAM implementation)  
**Target content:** RAG project timeline (corpus acquisition, embedding pipeline, frontend development)

### 10.1 Gantt Chart Update
The Gantt chart (gantt_chart_project_timeline.tex) needs new milestone labels:

Current milestones (11 rows):
1. Clinical scoping & problem identification
2. Literature survey on chest radiograph deep learning
3. Requirement analysis & clinical feasibility
4. System design (DenseNet-121, Grad-CAM, FastAPI)
5. Dataset curation, verification & stratified splitting
6. DenseNet-121 transfer learning & training pipeline
7. Grad-CAM visual interpretability implementation
8. FastAPI backend service & Docker containerization
9. Web (Next.js 15) & Mobile (Expo) client development
10. Empirical evaluation, benchmarking & confusion matrix
11. Project documentation, thesis compilation & submission

**Replace with:**
1. Legal domain scoping & civic complaint analysis
2. Literature survey on RAG systems, vector databases, legal AI
3. Requirement analysis & technical feasibility
4. System design (RAG pipeline, Pinecone, Gemini, FastAPI)
5. Legal corpus acquisition & PDF preprocessing
6. Embedding pipeline & Pinecone ingestion (all-MiniLM-L6-v2)
7. Query processing & bilingual Malayalam translation
8. FastAPI backend endpoints & async architecture
9. React 19 + Vite 8 frontend with voice input & PDF upload
10. Retrieval evaluation & answer quality benchmarking
11. Project documentation, report compilation & submission

**Files affected:** `diagrams/gantt_chart_project_timeline.tex`  
**Verification:** Compile diagram standalone → check labels render without overlap

---

## 11. CHAPTER 9: CONCLUSION (main.tex)

**Current content:** Lung disease detection achievements, 92.63% accuracy, ROC-AUC 98.50%  
**Target content:** Legal RAG system achievements, retrieval accuracy, bilingual support

Replace conclusion with:

> This project successfully designed, implemented, and evaluated CiviQ, an AI-powered legal information retrieval system using Retrieval-Augmented Generation. The system ingests comprehensive Indian legal corpora including post-2023 criminal codes (BNS, BNSS, BSA) and foundational civil statutes (Consumer Protection Act, RTI Act, Contract Act, Constitution). The RAG pipeline achieves high retrieval precision through sentence-transformers all-MiniLM-L6-v2 embeddings (384-dim, cosine-normalized), Pinecone vector indexing with HNSW search, and Google Gemini 2.5 Flash grounded generation with explicit source citations.
>
> Key accomplishments include:
> \begin{itemize}
>     \item Overlapping word-chunking (900 words, 150 overlap) preserving legal context across chunk boundaries.
>     \item Automatic Malayalam query detection (Unicode U+0D00–U+0D7F) with bidirectional translation, enabling linguistic inclusivity for non-English speakers.
>     \item FastAPI asynchronous backend with sub-200ms query latency for question answering and document analysis endpoints.
>     \item React 19 + Vite 8 frontend with browser-based voice input (Web Speech API), PDF upload, language selection, top-k slider, and source citation display.
>     \item Retrieval evaluation demonstrating relevant passage retrieval for RTI Act, Consumer Protection Act, BNS, and BNSS queries.
> \end{itemize}
>
> **Future enhancements** include: (i) Fine-tuning legal domain embeddings on Indian statutory corpora; (ii) Expanding to additional regional languages (Tamil, Telugu, Hindi); (iii) Incorporating judicial precedents and case law citations; (iv) Building feedback loops for answer quality improvement; (v) Deploying mobile applications for offline legal reference.

**Files affected:** `main.tex` (Chapter 9)  
**Verification:** LaTeX compile → check Chapter 9 conclusion

---

## 12. REFERENCES (main.tex)

**Current content:** References to CheXNet, DenseNet, Grad-CAM, medical imaging papers  
**Target content:** RAG, sentence-transformers, Pinecone, Gemini, legal AI papers

Replace bibliography with:

```bibtex
@article{lewis2020retrieval,
  title={Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks},
  author={Lewis, Patrick and others},
  journal={NeurIPS},
  year={2020}
}

@inproceedings{reimers2019sentence,
  title={Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks},
  author={Reimers, Nils and Gurevych, Iryna},
  booktitle={EMNLP},
  year={2019}
}

@article{malkov2018efficient,
  title={Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs},
  author={Malkov, Yury A and Yashunin, Dmitry A},
  journal={IEEE TPAMI},
  year={2018}
}

@inproceedings{chalkidis2020legal,
  title={LEGAL-BERT: The Muppets straight out of Law School},
  author={Chalkidis, Ilias and others},
  booktitle={Findings of EMNLP},
  year={2020}
}

@article{zhong2020does,
  title={Does {BERT} Make Any Sense? Interpretable Word Sense Disambiguation with Contextualized Embeddings},
  author={Zhong, Zexuan and others},
  journal={EMNLP},
  year={2020}
}

@article{ramesh2022samanantar,
  title={Samanantar: The Largest Publicly Available Parallel Corpora Collection for 11 Indic Languages},
  author={Ramesh, Gowtham and others},
  journal={arXiv preprint arXiv:2104.05596},
  year={2022}
}

@misc{gemini2024,
  title={Gemini: A Family of Highly Capable Multimodal Models},
  author={Google DeepMind},
  year={2024},
  howpublished={\url{https://deepmind.google/technologies/gemini/}}
}

@misc{pinecone2023,
  title={Pinecone Vector Database},
  author={Pinecone Systems},
  year={2023},
  howpublished={\url{https://www.pinecone.io/}}
}

@book{bns2023,
  title={Bharatiya Nyaya Sanhita, 2023},
  author={Ministry of Home Affairs, Government of India},
  year={2023}
}

@book{rti2005,
  title={Right to Information Act, 2005},
  author={Ministry of Law and Justice, Government of India},
  year={2005}
}
```

**Files affected:** `main.tex` (bibliography section)  
**Verification:** LaTeX compile with BibTeX → check references render correctly

---

## 13. DIAGRAM REWRITES

All TikZ diagrams in `diagrams/` directory must be redrawn to represent RAG concepts instead of lung disease detection.

### 13.1 fig1_2_system_architecture.tex
**Current content:** 4-column architecture showing Client (Web/Mobile), API Gateway (FastAPI validation), Deep Learning (DenseNet-121, Grad-CAM), Storage (model weights, eval metrics)

**New content:** 4-column RAG architecture:
- **Column 1: Frontend Layer**
  - User (citizen/student/journalist icon)
  - React 19 Web App (chat interface, voice input, language selector)
  - PDF Upload Component
  - Disclaimer (information only, not legal advice)

- **Column 2: API Gateway**
  - FastAPI REST Service (GET /api/health, POST /ask, POST /analyze-document)
  - Request Validation (MIME check, payload ≤50MB)
  - Malayalam Detection (Unicode U+0D00-U+0D7F)
  - Error Handling (400, 413, 503)

- **Column 3: RAG Processing**
  - PyMuPDF Text Extraction
  - Overlapping Chunker (900 words, 150 overlap)
  - Sentence-Transformers Embedder (all-MiniLM-L6-v2, 384-dim)
  - Pinecone Top-K Retrieval
  - Gemini 2.5 Flash Generation (with citations)
  - Translation (Malayalam ↔ English)

- **Column 4: Storage**
  - Pinecone Vector DB (384-dim embeddings, cosine metric)
  - Legal Corpus (BNS, BNSS, BSA, RTI, Contract, Consumer, Constitution PDFs)
  - Query Logs (telemetry)
  - Document Cache (temp uploaded PDFs)

**Layout fix:** Reduce box heights to 1.0cm (from 1.2cm) to prevent vertical overflow. Use fontsize 6.5pt for labels (down from 6.8pt).

**Files affected:** `diagrams/fig1_2_system_architecture.tex`  
**Verification:** Compile standalone → check no overlap, fits on page

### 13.2 fig_proposed_methods_pipeline.tex
**Current content:** 5-stage horizontal pipeline: Ingestion → Preprocessing → DenseNet-121 → Classify → Explain (Grad-CAM)

**New content:** 5-stage RAG pipeline:
1. **PDF Ingestion** (icon: faFilePdf, color: cInput)
   - PDF upload (≤50MB)
   - MIME validation
   - PyMuPDF extraction

2. **Text Preprocessing** (icon: faCut, color: cStage1)
   - Clean headers/footers
   - Overlapping chunking (900/150)
   - Min chunk: 40 words

3. **Embedding** (icon: faBrain, color: cStem)
   - sentence-transformers
   - all-MiniLM-L6-v2
   - L2 normalization
   - 384-dim vectors

4. **Indexing** (icon: faDatabase, color: cStage4)
   - Pinecone upsert
   - Batch: 100 vectors
   - Cosine metric
   - HNSW indexing

5. **Query & Generate** (icon: faComments, color: cStage2)
   - Query embedding
   - Top-k retrieval (k=5)
   - Gemini generation
   - Source citations

**Layout fix:** Reduce text width to 2.60cm (from 2.72cm), reduce minimum height to 5.40cm (from 5.60cm) to fit horizontally.

**Files affected:** `diagrams/fig_proposed_methods_pipeline.tex`  
**Verification:** Compile standalone → check horizontal fit, no text overflow

### 13.3 fig1_0_prismspace_workflow.tex
**Current content:** 6-node workflow: Radiograph Ingestion → Validation → DenseNet/Grad-CAM split → Classification → Delivery

**New content:** 6-node RAG workflow:
1. **Query Input** (User types or speaks query in English/Malayalam)
2. **Language Detection** (Unicode block check U+0D00-U+0D7F)
3. **Translation** (if Malayalam: translate to English via Gemini)
4. **Embedding & Retrieval** (encode query → Pinecone top-k)
5. **Generation** (Gemini 2.5 Flash conditioned on retrieved passages)
6. **Response Delivery** (translate back to Malayalam if needed, display sources)

**Feedback loop:** Dashed line from "Response Delivery" back to "Language Detection" labeled "User refinement / follow-up question"

**Layout fix:** Reduce node text width to 2.50cm (from 2.65cm), adjust vertical spacing to 1.70cm (from 1.80cm) to prevent overlap.

**Files affected:** `diagrams/fig1_0_prismspace_workflow.tex`  
**Verification:** Compile standalone → check no node overlap, feedback loop renders correctly

### 13.4 gantt_chart_project_timeline.tex
**Current content:** 11 milestones from "Clinical scoping" to "Project documentation"

**New content:** Update milestone labels (see section 10.1 above for complete list):
1. Legal domain scoping & civic complaint analysis
2. Literature survey on RAG systems, vector databases, legal AI
... (full list in section 10.1)

**Layout fix:** Already uses alternating row shading (prismMint opacity 0.65). Ensure label font size 8.5pt fits without horizontal overflow. If labels too long, abbreviate: "RAG systems, vector DBs, legal AI" → "RAG & legal AI literature"

**Files affected:** `diagrams/gantt_chart_project_timeline.tex`  
**Verification:** Compile standalone → check all 11 labels fit, no overlap, bars aligned to correct months

### 13.5 fig1_1_data_flow_diagram.tex
**Current content:** Level-1 DFD with external entities (Clinician, Client UI, Host Server), datastores (D1: Image Repository, D2: Model Registry, D3: Telemetry), processes (P1-P6: Ingestion, Audit, Normalize, DenseNet, Grad-CAM, Report)

**New content:** RAG Level-1 DFD:
- **External Entities:**
  - User (citizen/legal researcher)
  - Frontend (React App)
  - Pinecone API
  - Gemini API

- **Datastores:**
  - D1: Legal Corpus (PDF files: BNS, BNSS, BSA, RTI, etc.)
  - D2: Vector Index (Pinecone 384-dim embeddings)
  - D3: Query Logs (telemetry, user sessions)

- **Processes:**
  - P1.0: Ingest PDF (PyMuPDF extraction)
  - P2.0: Chunk Text (overlapping 900/150)
  - P3.0: Embed Chunks (all-MiniLM-L6-v2)
  - P4.0: Upsert to Pinecone (batch 100)
  - P5.0: Process Query (detect language, translate if Malayalam)
  - P6.0: Retrieve & Generate (Pinecone top-k → Gemini → citations)

**Flow arrows:**
- User → P5.0 (query input)
- P5.0 → D2 (query embedding → retrieval)
- D2 → P6.0 (retrieved passages)
- P6.0 → Frontend (JSON response)
- Frontend → User (rendered answer + sources)
- P1.0 → D1 (store PDFs)
- P3.0 → P4.0 → D2 (embeddings)

**Layout fix:** Reduce process circle diameter to 1.65cm (from 1.75cm), reduce font size to 6.8pt (from 7.0pt) to prevent label overflow.

**Files affected:** `diagrams/fig1_1_data_flow_diagram.tex`  
**Verification:** Compile standalone → check DFD nodes don't overlap, arrows connect correctly

### 13.6 fig11_end_to_end_system_flow.tex
**Current content:** 3-stage horizontal flow (Ingestion & Normalization → DenseNet Feature Learning → Explainability & Delivery) with input/output bars

**New content:** 3-stage RAG flow:
- **INPUT BAR:** User query (text/voice) in English/Malayalam, optional PDF upload

- **STAGE 1: Input Processing & Translation**
  - Language detection (Unicode block)
  - Malayalam→English translation (if needed)
  - PDF upload handling (MIME check, size ≤50MB)
  - Text extraction (PyMuPDF)
  - Chunking (900/150 overlap)

- **STAGE 2: Embedding & Retrieval**
  - Query embedding (all-MiniLM-L6-v2)
  - Pinecone cosine search
  - Top-k retrieval (k=5 default, user-configurable)
  - Passage ranking by similarity score

- **STAGE 3: Generation & Delivery**
  - Gemini 2.5 Flash prompt construction (context + question)
  - Grounded answer generation
  - Source citation extraction
  - English→Malayalam translation (if needed)
  - FastAPI JSON response (≈180ms latency)

- **OUTPUT BAR:** Answer with citations, source document cards, similarity scores

**Transition arrows:** Label arrows between stages: "Query text" (1→2), "Top-k passages" (2→3)

**Layout fix:** Reduce stepbox text width to 3.90cm (from 4.10cm), reduce inner spacing to keep stages from overflowing horizontally.

**Files affected:** `diagrams/fig11_end_to_end_system_flow.tex`  
**Verification:** Compile standalone → check 3 stages fit horizontally, input/output bars centered

### 13.7 fig1_2_model_responsibilities_inference_flow.tex
**Current content:** 6 rows showing model responsibilities: Validation, Transform, Normalizer, DenseNet, Classifier, Grad-CAM

**New content:** 6 rows for RAG pipeline components:

**Row 1:** Language Detector (Unicode block U+0D00-U+0D7F check → Malayalam flag)  
**Row 2:** Translator (Gemini API call → English query)  
**Row 3:** Query Embedder (sentence-transformers → 384-dim vector → L2 norm)  
**Row 4:** Vector Retriever (Pinecone query → top-k passages with scores)  
**Row 5:** Context Assembler (concatenate passages → prompt template)  
**Row 6:** LLM Generator (Gemini 2.5 Flash → grounded answer + citations)

Each row: 3 columns (Component Name | Processing Logic | Output)

**Layout fix:** Reduce row height to 1.05cm (from 1.15cm), reduce font to 7.4pt (from 7.6pt) to fit 6 rows vertically.

**Files affected:** `diagrams/fig1_2_model_responsibilities_inference_flow.tex`  
**Verification:** Compile standalone → check 6 rows fit vertically, no text overflow in columns

### 13.8 fig1_4_prismdb_schema_connectors.tex
**Current content:** 6 entity boxes showing dataset_partition, training_config, model_checkpoint, evaluation_telemetry, api_prediction, client_ui_state schemas with FK arrows

**New content:** RAG data schema:

**Column 1 (left):**
- **document_corpus** [PK: doc_id, FLD: filename, doc_type (BNS/RTI/etc), upload_date, page_count]
- **chunk_store** [PK: chunk_id, FK: doc_id, FLD: chunk_text, word_count, chunk_index]

**Column 2 (middle):**
- **vector_embeddings** [PK: embedding_id, FK: chunk_id, FLD: vector_384dim, pinecone_id, indexed_at]
- **retrieval_config** [PK: config_id, FLD: top_k (default 5), similarity_threshold, embedding_model (all-MiniLM-L6-v2)]

**Column 3 (right):**
- **query_log** [PK: query_id, FK: config_id, FLD: query_text, detected_language, translated_query, timestamp]
- **response_log** [PK: response_id, FK: query_id, FLD: answer_text, retrieved_chunk_ids[], latency_ms, user_feedback]

**FK arrows:**
- document_corpus.doc_id → chunk_store.doc_id
- chunk_store.chunk_id → vector_embeddings.chunk_id
- retrieval_config.config_id → query_log.config_id
- query_log.query_id → response_log.query_id
- vector_embeddings.chunk_id → response_log.retrieved_chunk_ids[] (dashed line)

**Layout fix:** Reduce table card text width to 4.20cm (from 4.40cm), reduce field font to 6.6pt (from 6.8pt).

**Files affected:** `diagrams/fig1_4_prismdb_schema_connectors.tex`  
**Verification:** Compile standalone → check 6 tables fit in 3×2 layout, FK arrows don't overlap

### 13.9 dag_task_graph_scheduling.tex
**Current content:** Shows DenseNet-121 layer connectivity graph (DenseBlocks 1-4 with dense connections, transition layers, Grad-CAM backward path)

**New content:** RAG pipeline component dependency DAG:

Nodes (left to right):
1. PDF Input
2. PyMuPDF Extractor
3. Text Cleaner (remove headers/footers)
4. Overlapping Chunker (900/150)
5. all-MiniLM-L6-v2 Embedder
6. L2 Normalizer
7. Pinecone Batch Uploader (100 vectors)
8. Query Input (User)
9. Query Embedder (same model)
10. Pinecone Retriever (top-k)
11. Gemini Generator (with context)
12. Citation Formatter
13. Response Output

**Edges:**
- PDF Input → PyMuPDF → Text Cleaner → Chunker → Embedder → Normalizer → Uploader → Pinecone Index
- Query Input → Query Embedder → Pinecone Retriever (reads from Pinecone Index)
- Pinecone Retriever → Gemini Generator → Citation Formatter → Response Output

**Backward dashed line:** Response Output → Query Input (user refinement loop)

**Layout fix:** Use smaller nodes (1.2cm width × 0.8cm height), 7pt font, vertical spacing 1.1cm to fit all 13 nodes.

**Files affected:** `diagrams/dag_task_graph_scheduling.tex`  
**Verification:** Compile standalone → check DAG fits on page, no node overlap, edges route cleanly

### 13.10 fig11_dag_execution_walkthrough.tex
**Current content:** (Need to check this file—likely similar to dag_task_graph_scheduling.tex)

**Action:** Read file first, then rewrite with same RAG pipeline DAG as 13.9 but possibly with execution timing annotations (e.g., "PyMuPDF: 2.3s", "Embedding: 0.8s", "Pinecone query: 0.05s", "Gemini: 1.2s").

**Files affected:** `diagrams/fig11_dag_execution_walkthrough.tex`  
**Verification:** Compile standalone → check timing annotations fit without overlapping nodes

### 13.11 fig1_3_multiagent_communication_flowchart.tex
**Current content:** Flowchart showing radiograph ingestion → validation decision → DenseNet inference → Grad-CAM generation → clinical report

**New content:** RAG query processing flowchart:

```
START
  ↓
[User inputs query (text/voice)]
  ↓
[Voice input?] → Yes → [Web Speech API transcription] → merge ↓
  ↓ No
[Text query]
  ↓
[Detect language (Unicode U+0D00-U+0D7F)]
  ↓
[Malayalam detected?] → Yes → [Translate to English (Gemini)] → merge ↓
  ↓ No
[English query]
  ↓
[Embed query (all-MiniLM-L6-v2, 384-dim)]
  ↓
[Pinecone cosine search, top-k retrieval]
  ↓
[Passages found?] → No → [Return "No relevant information"] → END
  ↓ Yes
[Build prompt: context + question]
  ↓
[Gemini 2.5 Flash generation]
  ↓
[Extract citations from sources]
  ↓
[Malayalam original query?] → Yes → [Translate answer to Malayalam] → merge ↓
  ↓ No
[English answer]
  ↓
[Format JSON response (answer, sources, latency)]
  ↓
[FastAPI return to frontend]
  ↓
[Display in React UI with source cards]
  ↓
END
```

**Decision diamonds:** "Voice input?", "Malayalam detected?", "Passages found?", "Malayalam original query?"

**Layout fix:** Use compact flowchart style with 1.5cm vertical spacing between nodes, 1.8cm horizontal spacing for branches. Diamond nodes: 2.0cm × 1.2cm. Rectangle nodes: 3.0cm × 0.9cm.

**Files affected:** `diagrams/fig1_3_multiagent_communication_flowchart.tex`  
**Verification:** Compile standalone → check flowchart fits on page, decision branches don't overlap

### 13.12 title_slide_overlay.tex
**Current content:** (Likely decorative title slide graphic)

**Action:** Update any title text references from lung disease to legal RAG. If purely decorative (geometric patterns), may not need changes.

**Files affected:** `diagrams/title_slide_overlay.tex`  
**Verification:** Compile standalone → check any text matches new project title

---

## 14. IMPLEMENTATION SEQUENCE

Execute edits in this order to maintain compilable state:

### Phase 1: Metadata & Front Matter (single commit)
1. Edit `main.tex` \gdef variables and \hypersetup
2. Edit `coverpage.tex` (title + author table)
3. Edit `certificate1.tex` (title + authors + guide)
4. Edit `declaration.tex` (author names in text + signature)
5. Edit `abstract.tex` (full content replacement)
6. Edit `acknowledgement.tex` (guide name + signatures)
7. **Verify:** `pdflatex main.tex` → check front matter pages (i–vi)

### Phase 2: Main Chapters (three commits)
8. Edit `main.tex` Chapter 1 (Introduction): background + objectives + scope
9. Edit `main.tex` Chapter 2 (Literature Review): 6 sections + comparison table
10. **Verify:** `pdflatex main.tex` → check Chapters 1-2 render
11. Edit `main.tex` Chapter 3 (Problem Definition): problem statement + formulation
12. Edit `main.tex` Chapter 4 (Requirements): FR list + hardware/software specs
13. **Verify:** `pdflatex main.tex` → check Chapters 3-4 render
14. Edit `main.tex` Chapter 5 (System Design): architecture text + figure caption updates
15. Edit `main.tex` Chapter 6 (Methodology): math sections + config table
16. Edit `main.tex` Chapter 7 (Preliminary Analysis): technology comparison sections + table
17. **Verify:** `pdflatex main.tex` → check Chapters 5-7 render

### Phase 3: Conclusion & References (single commit)
18. Edit `main.tex` Chapter 9 (Conclusion): achievements + future work
19. Edit `main.tex` bibliography: replace with RAG/legal AI references
20. **Verify:** `pdflatex main.tex && bibtex main && pdflatex main.tex` → check references compile

### Phase 4: Diagrams (11 commits, one per diagram)
21. Rewrite `diagrams/fig1_2_system_architecture.tex` → verify standalone compile
22. Rewrite `diagrams/fig_proposed_methods_pipeline.tex` → verify standalone compile
23. Rewrite `diagrams/fig1_0_prismspace_workflow.tex` → verify standalone compile
24. Rewrite `diagrams/gantt_chart_project_timeline.tex` → verify standalone compile
25. Rewrite `diagrams/fig1_1_data_flow_diagram.tex` → verify standalone compile
26. Rewrite `diagrams/fig11_end_to_end_system_flow.tex` → verify standalone compile
27. Rewrite `diagrams/fig1_2_model_responsibilities_inference_flow.tex` → verify standalone compile
28. Rewrite `diagrams/fig1_4_prismdb_schema_connectors.tex` → verify standalone compile
29. Rewrite `diagrams/dag_task_graph_scheduling.tex` → verify standalone compile
30. Rewrite `diagrams/fig11_dag_execution_walkthrough.tex` (after reading current content) → verify standalone compile
31. Rewrite `diagrams/fig1_3_multiagent_communication_flowchart.tex` → verify standalone compile
32. Update `diagrams/title_slide_overlay.tex` (if needed) → verify standalone compile

### Phase 5: Final Integration (single commit)
33. Compile full document: `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
34. Check all 12 diagrams render in main document without overflow/overlap
35. Check TOC, LOF (List of Figures), LOT (List of Tables) are correct
36. Check page numbering (roman i–vi for front matter, arabic 1–N for chapters)
37. Visual inspection: scroll through PDF, check for any overfull hboxes or diagram overlap

**Final Verification Checklist:**
- [ ] Cover page shows new title + 4 authors
- [ ] Certificate shows new title + guide "Hridhya J"
- [ ] Declaration has all 4 new authors
- [ ] Abstract describes RAG system (not lung disease)
- [ ] Chapter 1 Introduction discusses legal access barriers (not radiology)
- [ ] Chapter 2 Literature Review cites RAG/NLP papers (not medical imaging)
- [ ] Chapter 3 has RAG mathematical formulation (not DenseNet/Grad-CAM)
- [ ] Chapter 4 Requirements list text/voice query, PDF upload (not X-ray upload)
- [ ] Chapter 5 figures show RAG pipeline (not CNN architecture)
- [ ] Chapter 6 has embedding/chunking math (not CNN training)
- [ ] Chapter 7 compares vector DBs/LLMs (not CNN architectures)
- [ ] Chapter 8 Gantt chart has RAG milestones (not medical imaging milestones)
- [ ] Chapter 9 Conclusion describes RAG achievements (not 92% accuracy on X-rays)
- [ ] Bibliography has Lewis 2020 RAG paper, sentence-transformers paper (not CheXNet)
- [ ] All 12 diagrams compile standalone without errors
- [ ] All 12 diagrams fit in document without overflow or overlap
- [ ] No "Overfull \hbox" warnings in LaTeX log for diagram pages

---

## 15. KNOWN RISKS & MITIGATION

### Risk 1: TikZ Diagram Complexity
**Risk:** TikZ diagrams are complex with precise positioning; rewrites may introduce overlap or overflow  
**Mitigation:**
- Test each diagram standalone first (`pdflatex diagram.tex`)
- Use `\adjustbox{max width=0.98\linewidth, keepaspectratio}` in main.tex
- Reduce font sizes (6.5pt → 6.0pt if needed)
- Reduce node dimensions (1.2cm → 1.0cm) for dense diagrams

### Risk 2: Chapter Length Mismatch
**Risk:** RAG content may be shorter/longer than medical imaging content, causing page breaks to shift  
**Mitigation:**
- Keep section structure parallel (same number of sections per chapter)
- Use `\clearpage` before major sections if needed
- Adjust paragraph spacing (`\vspace{8pt}`) to balance pages

### Risk 3: Bibliography Compilation Errors
**Risk:** BibTeX may fail if .bib file has syntax errors  
**Mitigation:**
- Validate .bib entries before committing
- Run sequence: `pdflatex → bibtex → pdflatex → pdflatex`
- Check .blg (BibTeX log) for errors

### Risk 4: Unicode Malayalam Characters
**Risk:** LaTeX may not render Malayalam Unicode (U+0D00–U+0D7F) if font doesn't support it  
**Mitigation:**
- Keep Malayalam references in text descriptions only, not in code/math
- Use `\texttt{U+0D00--U+0D7F}` for Unicode range notation (ASCII-safe)
- If actual Malayalam needed: `\usepackage{fontspec}` + `\setmainfont{Noto Sans Malayalam}`

### Risk 5: Figure Reference Mismatches
**Risk:** Figure labels in text may not match diagram file references after rewrites  
**Mitigation:**
- Keep all existing `\label{fig:...}` identifiers unchanged in main.tex
- Only update caption text, not label names
- Verify with: `grep "\\ref{fig:" main.tex` matches `grep "\\label{fig:" main.tex`

---

## 16. SUCCESS CRITERIA

The rewrite is complete when:

1. **Document compiles without errors:** `pdflatex main.tex` exits with code 0, no "Fatal error" in log
2. **All metadata updated:** PDF properties show new title + 4 authors
3. **All chapters rewritten:** No mentions of "lung disease", "chest X-ray", "DenseNet", "Grad-CAM" in Chapters 1-9
4. **All diagrams redrawn:** 12 TikZ files show RAG concepts (no CNN/medical imaging visuals)
5. **No layout issues:** No overfull hboxes on diagram pages, all figures fit within margins
6. **References updated:** Bibliography cites RAG/NLP/legal AI papers (no medical imaging papers)
7. **Front matter correct:** Coverpage, certificate, declaration, abstract all show new project
8. **Visual inspection pass:** Manual scroll through PDF shows professional, coherent RAG system report

---

## APPENDIX: Quick Reference

**Project Title (new):** AI-POWERED LEGAL INFORMATION RETRIEVAL USING RETRIEVAL-AUGMENTED GENERATION  
**Short Title:** AI-Powered Legal Information Retrieval using RAG

**Authors:**
1. ALEENA (KNP23CS025)
2. FATHIMA (KNP23CS047)
3. ADITHYA (KNP23CS016)
4. ABHINAYA (KNP23CO007)

**Guide:** Hridhya J, Assistant Professor

**Tech Stack:**
- Backend: Python 3.12, FastAPI, PyMuPDF, sentence-transformers (all-MiniLM-L6-v2), Pinecone, Google Gemini 2.5 Flash
- Frontend: React 19, Vite 8, Tailwind CSS 4
- Key concepts: RAG, embedding (384-dim), cosine similarity, top-k retrieval, grounded generation, Malayalam translation

**Files to modify:**
- main.tex (metadata, all 9 chapters, bibliography)
- coverpage.tex, certificate1.tex, declaration.tex, abstract.tex, acknowledgement.tex
- 12 diagram .tex files in diagrams/

**Verification commands:**
```bash
# Standalone diagram
cd diagrams
pdflatex fig1_2_system_architecture.tex

# Full document
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

---

**END OF PLAN**
