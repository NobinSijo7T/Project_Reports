# -*- coding: utf-8 -*-
"""
Script to restructure Report/main.tex into the 9-chapter KTU/CEK B.Tech CSE Project Report Format
as specified by the reference profile JSON.
Preserves 100% of PrismSpace technical content, figures, tables, math, code, and references.
"""

import os
import re

with open("Report/main_backup_before_restructure.tex", "r", encoding="utf-8") as f:
    orig = f.read()

# Preamble up to \begin{document}
preamble_end = orig.find("\\begin{document}")
if preamble_end == -1:
    raise ValueError("Could not find \\begin{document}")

preamble = orig[:preamble_end].strip()

# Adjust preamble: ensure front matter has page numbers
# In front matter, ensure \pagestyle{plain} so roman numerals (i, ii, iii...) appear on all pages.

front_matter = r"""
\begin{document}

%------------------------------------------------------------------------------
% FRONT MATTER
%------------------------------------------------------------------------------
\hypersetup{pageanchor=false}
\include{coverpage}
\include{certificate1}
\include{declaration}
\hypersetup{pageanchor=true}

\cleardoublepage
\pagenumbering{roman}
\pagestyle{plain}

\include{abstract}
\include{acknowledgement}

\cleardoublepage
\tableofcontents
\cleardoublepage
\listoffigures
\cleardoublepage
\listoftables
\cleardoublepage

\include{symbol}

%------------------------------------------------------------------------------
% MAIN BODY (Arabic Numbering & Header/Footer)
%------------------------------------------------------------------------------
\cleardoublepage
\setcounter{page}{1}
\pagenumbering{arabic}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\fontsize{9}{11}\selectfont \textit{\shorttitle}}
\fancyhead[R]{\fontsize{9}{11}\selectfont \textit{\deptabbr, CEK}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
"""

# Extract Chapter 1 parts
# In original, Chapter 1 goes from:
# \chapter[Introduction]{\Huge Introduction}
# to \chapter{Literature Review}

chap1_text = r"""
%==============================================================================
% CHAPTER 1: INTRODUCTION
%==============================================================================
\chapter[Introduction]{\Huge Introduction}

In contemporary software engineering, developers are inundated with an ever-expanding array of fragmented tools, communication channels, execution environments, and knowledge silos. Modern software delivery demands constant context switching across source code editors, cloud terminals, database inspectors, cryptographic validators, API testbeds, and external documentation hubs. Cognitive studies consistently demonstrate that frequent context-switching significantly degrades engineering throughput, introduces subtle syntactic and semantic bugs, and amplifies mental fatigue.

Simultaneously, the dawn of generative artificial intelligence and Large Language Models (LLMs) has sparked a fundamental paradigm shift in human-computer interaction. Autonomous coding assistants, multi-agent frameworks, and conversational copilot interfaces now possess the capability to generate code snippets, formulate complex execution plans, invoke external tools, and diagnose intricate runtime failures. However, despite their theoretical promise, existing agentic solutions suffer from several crippling architectural shortcomings:
\begin{enumerate}[(i)]
    \item \textbf{Monolithic and Opaque Black-Box Execution:} Commercial AI coding solutions frequently execute actions invisibly on remote servers without granular step-by-step observability, structured intermediate state inspections, or verifiable human-in-the-loop checkpoints.
    \item \textbf{Single-Provider Monopolization and Prohibitive Costs:} Relying exclusively on a single proprietary LLM provider leads to severe vendor lock-in, unmitigated rate limits, and unsustainable operational expenditures for routine developer queries.
    \item \textbf{Lack of Protocol Standardization for External Tool Invocations:} Traditional tool-use agent implementations rely on brittle ad-hoc prompt engineering or proprietary function schemas, which fail to generalize across diverse operating system utilities, sandboxed execution runtimes, and local developer file trees.
    \item \textbf{Fragile, Transient Client State Persistence:} Most web-based developer dashboards fail to implement robust offline-first, client-side transactional storage, rendering developer notes, tool execution history, and active swarm trajectories volatile.
\end{enumerate}

To comprehensively solve these critical engineering challenges, this project introduces \textbf{PrismSpace}: an intelligent, local-first developer operating environment and multi-agent orchestration platform. PrismSpace bridges a high-performance modern browser dashboard with a dedicated Python orchestration backend implementing the open \textbf{Model Context Protocol (MCP)} and an end-to-end Machine Learning routing, planning, and safety subsystem.

\section{Background and Overview}
The software development lifecycle encompasses diverse activities: conceptual design, requirements engineering, rapid prototyping, unit testing, schema migration, bug localization, and security audits. To support these diverse workflows within a single coherent workspace, PrismSpace unifies 23+ purpose-built developer utilities into an elegant desktop-class interface while embedding an autonomous \textit{Agent Swarm} orchestration layer.

At the core of the Agent Swarm lies a decoupled, multi-tiered architecture. Rather than routing all developer prompts blindly to expensive frontier models, PrismSpace deploys an intelligent ML policy pipeline. Incoming natural language queries are parsed through calibrated lexical and semantic feature extractors, classified into specific execution intents, mapped to optimal agent personas, and routed to the most cost-effective and capable foundation model provider---including Groq for ultra-low latency inference, NVIDIA NIM for sovereign accelerated execution, Anthropic for safety-critical reasoning, and OpenAI or Google Gemini for broad generative synthesis.

\section{Standard Agent Baselines and Their Limitations}
Traditional developer tools and early autonomous agent copilot implementations typically adopt a linear, single-model approach: developer prompts are forwarded directly to a monolithic remote LLM, which attempts to return text or tool-call JSON in an unconstrained single turn. This baseline architecture reveals severe structural limitations when deployed in complex engineering workflows:
\begin{itemize}
    \item \textbf{Lack of Iterative Decomposition:} Complex engineering tasks (e.g., refactoring an entire microservice or conducting multi-source competitive benchmarking) exceed the reliable context window and reasoning horizons of single-turn generation, resulting in hallucinated imports, omitted edge cases, and incomplete execution.
    \item \textbf{Absence of Verification Checkpoints:} Baseline tools execute commands without evaluating potential file destruction or irreversible shell executions, risking catastrophic data loss or repository corruption.
    \item \textbf{Excessive Token Costs on Simple Tasks:} Forwarding mundane operations (such as regex linting or JSON formatting) to frontier LLMs incurs unnecessary billing and introduces hundreds of milliseconds of network latency.
\end{itemize}

\section{PrismSpace: Intelligent Developer Operating Environment}
PrismSpace re-architects the developer workspace around three foundational pillars: (1) a client-side reactive operating environment housing 23+ offline utilities with sub-millisecond local state persistence via IndexedDB (\textbf{PrismDB}); (2) a multi-provider Machine Learning intelligence tier executing calibrated intent classification, predictive routing, and safety gating; and (3) an autonomous multi-agent swarm that decomposes high-level goals into Directed Acyclic Graphs (DAGs), executing parallel worker threads over the standardized Model Context Protocol (MCP).

\section{Objectives of the Project}
The specific engineering and research objectives of this project are:
\begin{enumerate}
    \item To build a responsive, desktop-grade web application using \textbf{Next.js 15}, \textbf{React 19}, and \textbf{Tailwind CSS}, housing an integrated Dev Space with 23+ developer, AI, and productivity tools.
    \item To architect a client-side, ACID-compliant database layer (\textbf{PrismDB}) using \textbf{Dexie.js} and browser \textbf{IndexedDB}, providing sub-50ms reactive state queries via \texttt{useLiveQuery}.
    \item To engineer a high-throughput Python \textbf{FastAPI Hive Backend} implementing the \textbf{Model Context Protocol (MCP)} to standardize agent tool discovery, sandboxed execution, and Server-Sent Events (SSE) telemetry streaming.
    \item To formulate and train a multi-stage Machine Learning subsystem comprising:
    \begin{itemize}
        \item A 12-class \textit{Intent Classifier} operating on TF-IDF lexical n-grams.
        \item An adaptive \textit{Multi-Provider Router} that dynamically selects optimal foundation model endpoints.
        \item A multi-label \textit{Agent Swarm Dispatcher} that activates specialized agent personas.
        \item A threshold-calibrated \textit{Human-in-the-Loop Safety Gate} for anomaly detection and approval prediction.
        \item Gradient boosted regressors for predictive task execution \textit{latency} and \textit{monetary cost} estimation.
        \item Single-stage preference alignment via \textit{Odds Ratio Preference Optimization (ORPO)} with Low-Rank Adapters (LoRA).
    \end{itemize}
    \item To benchmark and evaluate the complete system across industry standard datasets, demonstrating superior task completion accuracy, low routing error, robust safety gating, and minimal computational overhead.
\end{enumerate}

\section{Scope and Impact}
PrismSpace is designed for software engineers, systems researchers, web developers, and technical operators who require a local-first, highly customizable developer workspace. By providing complete step-by-step transparency into agent planning, dynamic DAG decomposition, and sandboxed tool execution, PrismSpace shifts autonomous AI from an opaque black box into an auditable, trustworthy engineering copilot. The open MCP architecture ensures seamless extensibility with third-party developer tool servers, including GitHub, PostgreSQL, Docker, and headless browser automation.

\section{Organization of the Report}
The remainder of this report is organized as follows:
\begin{itemize}
    \item \textbf{Chapter 2 (Literature Review):} Reviews theoretical foundations in multi-agent reinforcement learning, dynamic role discovery, cloud workflow scheduling, standardized tool protocols, preference alignment, and local-first data architectures, highlighting critical research gaps.
    \item \textbf{Chapter 3 (Problem Definition):} Formalizes the problem statement, details the core engineering challenges, delineates project scope and constraints, and establishes the mathematical graph optimization problem formulation.
    \item \textbf{Chapter 4 (Requirements Specification):} Presents the formal System Requirements Specification (SRS), encompassing detailed functional requirements, non-functional quality attributes, and hardware/software specifications.
    \item \textbf{Chapter 5 (System Design):} Details the high-level 6-tier architecture, system workflow, multi-agent framework, end-to-end flow, execution flowchart, DAG scheduling walkthrough, database schema, and Level-1 Data Flow Diagram (DFD).
    \item \textbf{Chapter 6 (Preliminary Analysis):} Analyzes foundational principles, algorithms, mathematical formulations (SGD, GAT, ORPO), and provides technical rationale for frontend, database, backend, and machine learning technology selections.
    \item \textbf{Chapter 7 (Design and Methodology):} Details benchmark data curation, the multi-stage machine learning pipeline design, staged inference flow, frontend dev space utilities, Dexie.js persistence, and evaluation metrics definitions.
    \item \textbf{Chapter 8 (Result \& Observation):} Analyzes empirical experimental results across benchmark datasets, reports classification accuracy, safety gate calibration, latency profiling, software verification, and project feasibility.
    \item \textbf{Chapter 9 (Conclusion and Future Scope):} Summarizes the major engineering achievements, discusses current constraints, and outlines prospective research directions.
\end{itemize}
"""

# Extract Chapter 2: Literature Review exactly as is
chap2_start = orig.find("\\chapter{Literature Review}")
chap2_end = orig.find("\\chapter{System Requirements and Architecture Specification}")
if chap2_start == -1 or chap2_end == -1:
    raise ValueError("Could not find Chapter 2 boundaries")

chap2_body = orig[chap2_start:chap2_end].strip()

# Now create Chapter 3: Problem Definition
# It incorporates the Problem Statement, Problem Description (the 4 root challenges),
# Scope and Objectives, and Theoretical Problem Formulation!
chap3_text = r"""
%==============================================================================
% CHAPTER 3: PROBLEM DEFINITION
%==============================================================================
\chapter{Problem Definition}

A rigorous engineering formulation is essential to transform broad software development challenges into actionable, verifiable system requirements. This chapter establishes the formal problem statement, details the root technical challenges confronting modern developer workflows, defines the precise project scope and boundary constraints, and presents the mathematical problem formulation governing multi-agent swarm scheduling and safety gating.

\section{Problem Statement}
Contemporary developer workspaces lack a unified, local-first environment that seamlessly combines day-to-day software utilities with an observable, cost-optimized, and protocol-standardized multi-agent orchestration engine. Developers are forced to juggle disconnected standalone tools, absorb opaque and expensive LLM API invocations without intelligent routing, and risk unchecked tool execution side-effects without calibrated safety checkpoints. 

The objective of this project is to design, implement, and evaluate \textbf{PrismSpace}: an open-source, full-stack developer operating environment featuring an intelligent multi-agent swarm system, an open Model Context Protocol (MCP) tool execution bridge, a multi-stage machine learning routing and alignment subsystem, and a reactive browser database architecture.

\section{Problem Description}
Modern software engineering requires navigating intricate, multi-dimensional workflows. When examined in detail, the core limitations of existing developer environments stem from four root challenges:
\begin{enumerate}
    \item \textbf{Cognitive Fragmentation across Disconnected Tools:} Modern developers constantly switch contexts between source code editors, cloud terminals, database viewers, regex testbeds, and external documentation portals. Each transition imposes a cognitive penalty, fragments local scratchpad notes, and increases bug frequency.
    \item \textbf{Opaque and Unobservable Agent Execution:} Commercial copilot solutions process developer requests remotely inside closed proprietary clouds. The developer receives only a finalized code block without access to intermediate thought traces, DAG sub-task decomposition, or tool invocation parameters, rendering debugging and verification intractable.
    \item \textbf{Runaway Model Inference Expenditures and Latency:} Blindly dispatching every developer prompt to frontier LLM APIs (e.g., Claude 3.5 Sonnet or GPT-4o) incurs unsustainable monetary costs and introduces latency penalties of up to several seconds for trivial syntactic transformations that could execute near-instantaneously on smaller or specialized models.
    \item \textbf{Uncalibrated Security and Data Privacy Risks:} Granting autonomous agents direct access to filesystem modifications and terminal command execution introduces significant security hazards. Existing frameworks either block tool execution entirely or permit unrestricted execution without automated risk assessment or human confirmation checkpoints. Furthermore, transmitting proprietary source code and private credentials to external third-party cloud databases violates enterprise data sovereignty.
\end{enumerate}

\section{Scope and Objectives}
PrismSpace defines clear operational boundaries designed to maximize utility while maintaining local privacy and execution safety:
\begin{itemize}
    \item \textbf{In-Scope Capabilities:}
    \begin{itemize}
        \item Deployment of a desktop-grade browser interface housing 23+ offline developer utilities.
        \item Implementation of a client-side ACID database (\textbf{PrismDB}) using IndexedDB and Dexie.js for sub-50ms reactive state queries.
        \item Engineering an asynchronous Python FastAPI Hive bridge implementing the Model Context Protocol (MCP).
        \item Construction and training of an intelligent ML routing subsystem predicting intent, optimal provider, latency, and monetary cost.
        \item Implementation of a threshold-calibrated Human-in-the-Loop Safety Gate for destructive action containment.
        \item Execution of Directed Acyclic Graph (DAG) task scheduling across concurrent worker personas.
    \end{itemize}
    \item \textbf{Out-of-Scope and System Constraints:}
    \begin{itemize}
        \item Direct training of multi-billion parameter foundation LLMs from scratch (pre-trained frontier endpoints and LoRA adapters are utilized).
        \item Full container virtualization within purely sandboxed WebAssembly environments (subprocess-level isolation via MCP is employed).
    \end{itemize}
\end{itemize}

\section{Theoretical Problem Formulation}
Let the multi-agent system be formalized as a dynamic graph $\mathcal{G} = (V, E, \mathbf{A})$, where $V = \{v_1, \dots, v_N\}$ denotes the set of $N$ heterogeneous entities comprising specialized agent personas and accessible MCP tool servers. The set $E \subseteq V \times V$ represents directed communication and dependency channels between complementary agent roles, parameterized by an adjacency matrix $\mathbf{A} \in \{0, 1\}^{N \times N}$.

Given a developer task specification $\mathcal{T}_{\text{task}}$, the objective is to determine an optimal routing assignment $\mathbf{y}_{\text{route}}^*$, a subset of active swarm workers $V_{\text{active}} \subseteq V$, and an execution schedule DAG that minimizes total monetary cost $\mathcal{C}$ and latency $\mathcal{L}$ while maximizing task completion fidelity $\mathcal{S}_{\text{fidelity}}$ under strict safety constraints:
\begin{equation}
    \max_{V_{\text{active}}, \mathbf{y}_{\text{route}}} \quad \mathcal{S}_{\text{fidelity}}(\mathcal{T}_{\text{task}}) - \lambda_1 \mathcal{C}(\mathbf{y}_{\text{route}}) - \lambda_2 \mathcal{L}(\mathbf{y}_{\text{route}})
\end{equation}
\begin{equation}
    \text{subject to} \quad \mathcal{P}_{\text{harm}}(v_i, a_j) \le \tau_{\text{safety}}, \quad \forall v_i \in V_{\text{active}}, \; a_j \in \mathbf{A}_{i,j}
\end{equation}
where $\mathcal{P}_{\text{harm}}$ denotes the predicted risk probability of action $a_j$ initiated by agent $v_i$, and $\tau_{\text{safety}}$ is the calibrated safety decision threshold.
"""

# Extract Chapter 4: Requirements Specification
# Functional Requirements (Table), Non-Functional Requirements (Table), System Requirements
chap4_text = r"""
%==============================================================================
% CHAPTER 4: REQUIREMENTS SPECIFICATION
%==============================================================================
\chapter{Requirements Specification}

A robust software engineering project necessitates rigorous requirements modeling, formal environmental constraints, and clearly specified operational parameters. This chapter presents the System Requirements Specification (SRS), formalizing the functional capabilities, non-functional quality attributes, and host hardware/software deployment environments.

\section{Functional Requirements}
Functional requirements define the core behaviors, services, and operational reactions that PrismSpace must provide to the user and interacting subsystems. Table~\ref{tab:functional_requirements} summarizes the primary functional requirements.

\begin{table}[H]
\centering
\caption{PrismSpace Functional Requirements Specification.}
\label{tab:functional_requirements}
\small
\begin{tabularx}{\textwidth}{l p{3.8cm} X}
\toprule
\textbf{Req. ID} & \textbf{Requirement Name} & \textbf{Operational Description} \\
\midrule
\textbf{FR-01} & Integrated Developer Workspace & The system shall provide an application shell housing 23+ developer tools spanning general utility, AI assistants, and productivity widgets. \\
\textbf{FR-02} & Agent Swarm Launch \& Config & The system shall allow users to formulate natural language objectives, configure worker agents ($K \le 5$), select providers, and toggle safety gating. \\
\textbf{FR-03} & Intelligent ML Model Routing & The system shall extract lexical and semantic features to predict intent, route to the optimal provider (Groq, NIM, OpenAI, Anthropic), and estimate latency/cost. \\
\textbf{FR-04} & MCP Tool Standard Integration & The backend shall discover, authenticate, and manage local MCP tool servers (Filesystem, Terminal, GitHub, Browser), exposing structured schemas to agents. \\
\textbf{FR-05} & Human-in-the-Loop Checkpoint & When an agent initiates an action classified as ambiguous or destructive, the system shall transition to \texttt{waiting\_approval} and pause until confirmed. \\
\textbf{FR-06} & Real-Time Telemetry Streaming & The system shall stream real-time thought traces, tool invocations, stdout logs, and final deliverables to the client via Server-Sent Events (SSE). \\
\textbf{FR-07} & Reactive Offline-First Storage & All user configurations, session chats, tool histories, checklists, and habits shall persist locally within browser IndexedDB, accessible without network. \\
\bottomrule
\end{tabularx}
\end{table}

\section{Non-Functional Requirements}
Non-functional requirements specify the system quality attributes, operational performance ceilings, security postures, and architectural constraints. Table~\ref{tab:non_functional_requirements} specifies the non-functional requirements.

\begin{table}[H]
\centering
\caption{PrismSpace Non-Functional Requirements Specification.}
\label{tab:non_functional_requirements}
\small
\begin{tabularx}{\textwidth}{l p{3.5cm} X}
\toprule
\textbf{Req. ID} & \textbf{Quality Attribute} & \textbf{Performance Target / Operational Standard} \\
\midrule
\textbf{NFR-01} & Latency Performance & Client database reads via \texttt{useLiveQuery} shall execute in $<50$ ms. ML routing inference shall conclude in $<150$ ms on CPU/GPU. \\
\textbf{NFR-02} & Privacy \& Sovereignty & Workspace notes, API tokens, and local database tables shall remain strictly resident on the host machine. Zero unencrypted third-party cloud telemetry. \\
\textbf{NFR-03} & Reliability \& Resilience & The agent loop shall incorporate exponential backoff, schema retry mechanisms, and graceful fallbacks when external LLM endpoints experience outages. \\
\textbf{NFR-04} & Modularity \& Extensibility & The system shall adhere strictly to decoupled interfaces, allowing addition of new MCP tools, ML classifiers, and UI panels without refactoring core logic. \\
\bottomrule
\end{tabularx}
\end{table}

\section{System Requirements}
The operational environment specifications for developing, training, and running PrismSpace across host workstations are detailed in Table~\ref{tab:system_specs}.

\subsection{Hardware and Software Requirements}
\begin{table}[H]
\centering
\caption{System Environment and Development Specifications.}
\label{tab:system_specs}
\small
\begin{tabularx}{\textwidth}{lX}
\toprule
\textbf{Attribute} & \textbf{Specification Details} \\
\midrule
\textbf{Processor (CPU)} & AMD Ryzen 7 / Intel Core i7 (8 Cores, 16 Threads, $\ge 3.8$ GHz) \\
\textbf{Memory (RAM)} & 24 GB DDR4/DDR5 High-Speed RAM \\
\textbf{Graphics (GPU)} & NVIDIA GeForce RTX 3050A / 4060 with CUDA Compute Capability $\ge 8.6$ \\
\textbf{Host Operating System} & Microsoft Windows 11 64-bit / Linux Ubuntu 22.04 LTS \\
\textbf{Frontend Framework} & Next.js 15.0+ (App Router), React 19.0, TypeScript 5.7+ \\
\textbf{Styling Engine} & Tailwind CSS 3.4+, PostCSS, Framer Motion, GSAP \\
\textbf{Client Database} & Dexie.js v3.2+ over Browser IndexedDB API (WASM SQLite optional) \\
\textbf{Backend Framework} & Python 3.10+, FastAPI 0.115+, Uvicorn ASGI Server \\
\textbf{Machine Learning Stack} & PyTorch 2.5 (CUDA 12.6), scikit-learn 1.5, XGBoost 2.1, HuggingFace TRL \\
\textbf{Protocol Standard} & Model Context Protocol (MCP) JSON-RPC 2.0 Specification \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Databases and Storage}
PrismSpace utilizes a client-side relational storage engine (\textbf{PrismDB}) built on top of the browser's native IndexedDB standard using Dexie.js. This eliminates cloud database hosting costs, guarantees zero-latency offline operation, and ensures complete privacy for proprietary developer codebases.

\subsection{Libraries and Frameworks}
The machine learning and backend pipeline leverages PyTorch 2.5 for neural computations, scikit-learn for calibrated linear intent classifiers and TF-IDF vectorization, XGBoost for gradient-boosted regression, HuggingFace TRL for ORPO preference alignment, and FastAPI with Pydantic for high-throughput asynchronous API handling.

\subsection{Front-End Interaction Layer}
The user interface is built on Next.js 15 utilizing React 19 concurrent features, TypeScript 5.7, Tailwind CSS for zero-runtime utility styling, and \texttt{react-rnd} for floating, draggable desktop window primitives.
"""

# Now Chapter 5: System Design
# Incorporates:
# 5.1 High-Level Architecture (Figure 5.1: 6-Tier Architecture)
# 5.2 System Workflow and Multi-Agent Framework
#     5.2.1 Multi-Agent Framework (Figure 5.2, fig_proposed_methods_pipeline)
#     5.2.2 Layered System Workflow (Figure 5.3, fig1_0_prismspace_workflow)
#     5.2.3 End-to-End System Flow Architecture (Figure 5.4, fig11_end_to_end_system_flow)
# 5.3 System Flowchart and Algorithms
#     5.3.1 Multi-Agent Swarm Flowchart (Figure 5.5, fig1_3_multiagent_communication_flowchart)
#     5.3.2 System Algorithm (Step-by-step Algorithm 1)
#     5.3.3 DAG Task Graph Scheduling Pipeline (Figure 5.6, dag_task_graph_scheduling)
# 5.4 Detailed Component Analysis
#     5.4.1 Client-Side Reactive Storage Schema (PrismDB) (Figure 5.7, fig1_4_prismdb_schema_connectors)
#     5.4.2 Level-1 Data Flow Architecture (Figure 5.8, fig1_1_data_flow_diagram)

chap5_text = r"""
%==============================================================================
% CHAPTER 5: SYSTEM DESIGN
%==============================================================================
\chapter{System Design}

This chapter establishes the architectural structure and operational logic governing PrismSpace. We examine the 6-tier system architecture, multi-agent framework, layered execution workflow, end-to-end system flow, multi-agent communication flowchart, the formal swarm scheduling algorithm with DAG execution walkthrough, client-side database schema, and the Level-1 Data Flow Diagram (DFD).

\section{High-Level Architecture}
PrismSpace is organized into six strictly decoupled architectural tiers designed for high-throughput developer collaboration and complete execution observability:
\begin{itemize}\setlength{\itemsep}{1.5pt}\setlength{\parsep}{0pt}\setlength{\topsep}{2pt}
    \item \textbf{Tier 1: Presentation Layer (Next.js 15 + React 19):} Houses the desktop app shell, glassmorphic HUD widgets, customizable clock styles, 23+ Dev Space utility panels, and the interactive Agent Swarm dashboard.
    \item \textbf{Tier 2: API Bridge and Gateway Layer (FastAPI Hive Bridge):} Exposes asynchronous REST endpoints, manages Server-Sent Event (SSE) streams, and orchestrates live MCP tool registrations.
    \item \textbf{Tier 3: Feature and Routing Layer (ML Policy Engine):} Extracts 10,000-dimensional TF-IDF lexical n-grams and 5D structural metrics, executing multi-class intent classification and multi-provider routing.
    \item \textbf{Tier 4: Multi-Agent Orchestration Layer (DAG Swarm Engine):} Decomposes high-level objectives into dependency DAGs, manages concurrent worker agents ($K \le 5$), and oversees the autonomous ReAct tool execution cycle.
    \item \textbf{Tier 5: Evaluation and Safety Layer (Human-in-the-Loop Gate):} Computes anomaly scores, evaluates completion safety log-odds, and enforces approval checkpoints before executing destructive operations.
    \item \textbf{Tier 6: Deployment and Persistence Layer (PrismDB + Foundation Models):} Persists relational records across 17 Dexie IndexedDB tables and coordinates inference across external LLM endpoints (Groq, NVIDIA, OpenAI, Anthropic).
\end{itemize}

Figure~\ref{fig:system_arch_detailed} illustrates the detailed multi-tier architectural topology of PrismSpace, highlighting the component boundaries and communication pipelines across the three primary operational pillars:

\begin{figure}[H]
    \centering
    \adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_2_system_architecture.tex}}
    \caption{Detailed multi-tier system architecture of PrismSpace illustrating Presentation, API Gateway, ML Hybrid Routing, Swarm DAG Orchestration, and Persistent Deliverables.}
    \label{fig:system_arch_detailed}
\end{figure}

As depicted in Figure~\ref{fig:system_arch_detailed}, the architecture maintains strict decoupling across three primary functional blocks:
\begin{enumerate}
    \item \textbf{Presentation and Gateway Column (Left):} Houses the responsive Next.js 15 client with React 19 server and client components, Monaco Editor, and Dexie.js local storage bridge. Client interactions are dispatched through Server-Sent Event (SSE) streaming connections to the FastAPI Hive Gateway (\texttt{hive\_api.py}), which orchestrates MCP tool registration and manages client-agent communication channels.
    \item \textbf{Machine Learning Routing and Hybrid Retrieval Column (Center):} Ingests parsed feature vectors and deploys a multi-provider model routing grid. Simple classification, code parsing, and syntactical transformations are routed to ultra-low latency Groq LPU endpoints running Llama 3.3 70B ($>300$ tokens/s). Complex architectural reasoning, multi-step debugging, and safety-critical tasks route to Anthropic Claude 3.5 Sonnet or OpenAI GPT-4o, while sovereign self-hosted workloads execute through NVIDIA NIM endpoints.
    \item \textbf{Swarm DAG Orchestration and Safety Column (Right):} The Workflow Planner dynamically decomposes user goals into an executable Directed Acyclic Graph (DAG) scheduled across specialist worker agents (Researcher, Data Agent, Writer, and Coder). Worker actions pass through a Safety Triad comprising an anomaly filter, policy critic, and human-in-the-loop (HITL) gate before generating verified deliverables (reports, pull requests, compiled code, and synchronized PrismDB records).
\end{enumerate}

\section{System Workflow and Multi-Agent Framework}

\subsection{Multi-Agent Framework and Swarm Hierarchy}
The comprehensive operational framework of PrismSpace is depicted in Figure~\ref{fig:framework}. The framework encompasses two complementary lifecycles: an \textbf{Offline Dataset Preprocessing and Training Phase} and an \textbf{Online Runtime Swarm Orchestration Phase}.

\begin{figure}[H]
    \centering
    \adjustbox{max width=0.98\linewidth, center}{\input{diagrams/fig_proposed_methods_pipeline.tex}}
    \caption{Proposed operational pipeline of PrismSpace multi-agent system.}
    \label{fig:framework}
\end{figure}

During offline training, multi-source benchmark datasets (LMSYS Chatbot Arena, RouterBench, WildGuardMix, UltraFeedback, and Agent Trajectories) undergo rigorous lexical extraction, z-score standardization, and isolation forest anomaly filtering. The resulting feature representations train the multi-head intelligence pipeline, including the intent classifier, provider router, safety gate, and ORPO alignment adapters. Figure~\ref{fig:framework} also shows the runtime path: the user prompt enters through the Next.js application, passes through the cognitive multi-agent layer, reaches the MCP execution layer, and is finally verified and persisted in PrismDB.

\subsection{Layered System Workflow}
Figure~\ref{fig:arch_workflow} illustrates the layered flow of execution traversing each architectural boundary within PrismSpace.

\begin{figure}[H]
    \centering
    \adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_0_prismspace_workflow.tex}}
    \caption{Architecture workflow and 6-stage execution lifecycle across PrismSpace system layers.}
    \label{fig:arch_workflow}
\end{figure}

Execution initiates in the React 19 Client Application, which dispatches requests through the reactive hooks layer to the FastAPI Hive Bridge Backend (\texttt{hive\_api.py}). Requests are parsed by the Feature Extraction and Vectorization engine into 10,000 TF-IDF n-grams augmented with 5D lexical metrics. The Multi-Head Intelligence Engine routes the prompt to the DAG Workflow Planner, which schedules parallel worker agents ($K \le 5$). Each worker executes an autonomous ReAct loop querying registered MCP tool endpoints. Intermediate states pass through the Approval and Safety Predictor before deliverables are persisted locally into Dexie IndexedDB tables and streamed to the user.

\subsection{End-to-End System Flow Architecture}
Figure~\ref{fig:system_flow} details the sequential algorithmic flow executed from the receipt of an objective prompt to final output rendering.

\begin{figure}[H]
    \centering
    \adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig11_end_to_end_system_flow.tex}}
    \caption{Overall end-to-end system flow architecture from prompt ingestion to validated deliverables.}
    \label{fig:system_flow}
\end{figure}

The pipeline in Figure~\ref{fig:system_flow} executes strictly sequentially, with the safety branch providing a controlled human-approval path:
\begin{enumerate}
    \item \textbf{Input Ingestion:} Natural language query and session constraints are ingested.
    \item \textbf{Preprocessing and Normalization:} Redundant whitespace, malformed Unicode, and out-of-distribution noise are scrubbed.
    \item \textbf{Feature Extraction:} 10k TF-IDF vocabulary features and numerical token lengths are synthesized into a unified tensor.
    \item \textbf{Missing Value Imputation:} Statistical medians and standard scalers normalize numeric dimensions.
    \item \textbf{Anomaly Detection:} IsolationForest filters adversarial outliers.
    \item \textbf{Multi-Model Intelligence Engine $\mathcal{M}_{\text{prism}}$:} Calibrated classifiers determine intent class, foundation provider, swarm workers, and safety requirements.
    \item \textbf{DAG Workflow Construction $\mathcal{L}_{\text{plan}}$:} Decomposes the task into an ordered dependency graph $\mathcal{G}(V, E)$.
    \item \textbf{ReAct Execution and MCP Loop:} Workers execute Observation $\to$ Thought $\to$ Action cycles.
    \item \textbf{Real-Time SSE Streaming:} Raw generated tokens and telemetry logs stream to the UI.
    \item \textbf{Evaluation and Verification:} Outputs are validated against ORPO preference reward benchmarks.
    \item \textbf{Local Persistence:} Complete session history and artifacts are saved to browser \texttt{PrismDB}.
\end{enumerate}

\section{System Flowchart and Algorithms}

\subsection{Multi-Agent Swarm Flowchart}
Figure~\ref{fig:multiagent_flowchart} details the comprehensive lifecycle, inter-agent communication protocols, and validation feedback mechanisms governing the multi-agent worker swarm:

\begin{figure}[H]
    \centering
    \adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_3_multiagent_communication_flowchart.tex}}
    \caption{Multi-agent communication and execution flowchart detailing objective ingestion, DAG planning, specialist swarm execution, verification gate, and adaptive re-planning feedback loop.}
    \label{fig:multiagent_flowchart}
\end{figure}

The execution dynamics in Figure~\ref{fig:multiagent_flowchart} operate across four structured stages:
\begin{enumerate}
    \item \textbf{Stage 1: User Objective and Intent Analysis:} Ingests user prompts, extracts lexical n-grams, and queries the calibrated classifier to resolve the execution scope and dispatch parameters.
    \item \textbf{Stage 2: DAG Planner and Dispatch Engine:} Translates the intent into a topological task graph, instantiates specialist agent personas, and assigns sub-task boundaries.
    \item \textbf{Stage 3: Multi-Agent Worker Swarm with MCP Tools:} Dispatches sub-tasks to concurrent specialist agents (Researcher, Coder, Reviewer) operating with registered MCP tool servers (filesystem, terminal, web scrapers).
    \item \textbf{Stage 4: Quality Check, HITL Review, and Delivery:} Runs evaluation rubrics and safety gating. If validation fails or tool execution encounters runtime exceptions, an automated feedback loop returns state to Stage 2 for dynamic DAG re-planning; otherwise, verified deliverables are persisted to PrismDB and delivered to the user.
\end{enumerate}

\subsection{System Algorithm}
The PrismSpace multi-agent swarm algorithm is structured into sequential operational steps, each governing a distinct phase of task ingestion, intelligent routing, collaborative agent execution, and verified state persistence.

\vspace{6pt}
\noindent\textbf{Step 1: System Initialization}
\vspace{4pt}

\noindent\begin{tabular}{p{1cm} p{12.5cm}}
1.1 & Load ML policy models: intent classifier, multi-label swarm dispatcher, cost/latency regressors, and safety gate logistic model. \\
1.2 & Initialize MCP tool registry: enumerate available filesystem, terminal, and web tool endpoints. \\
1.3 & Connect to PrismDB (IndexedDB via Dexie.js) and restore last agent session state if available. \\
1.4 & Establish FastAPI Hive Bridge with SSE streaming endpoint and configure CORS policy for local-first operation. \\
\end{tabular}

\vspace{6pt}
\noindent\textbf{Step 2: Task Input and Feature Extraction}
\vspace{4pt}

\noindent\begin{tabular}{p{1cm} p{12.5cm}}
2.1 & Receive natural language task specification $\mathcal{T}_{\text{task}}$ from the PrismSpace UI prompt interface. \\
2.2 & Compute lexical feature vector via TF-IDF with 5000-gram vocabulary on $\mathcal{T}_{\text{task}}$. \\
2.3 & Append numeric metadata features (token count, punctuation density, code keyword ratio) to form joint feature vector $\mathbf{x}_{\text{query}} \in \mathbb{R}^{5010}$. \\
 & \textit{Notation: $\mathcal{T}_{\text{task}}$ -- user task prompt; $\mathbf{x}_{\text{query}}$ -- joint prompt feature vector.} \\
\end{tabular}

\vspace{6pt}
\noindent\textbf{Step 3: Intent Classification and Multi-Provider Routing}
\vspace{4pt}

\noindent\begin{tabular}{p{1cm} p{12.5cm}}
3.1 & Pass $\mathbf{x}_{\text{query}}$ through the 12-class intent classifier to obtain provider probability distribution $\hat{\mathbf{y}}_{\text{route}} = \mathrm{softmax}(\mathbf{W}_{r}\mathbf{x}_{\text{query}} + \mathbf{b}_r)$. \\
3.2 & Select LLM provider $p^* = \arg\max_p \hat{y}_{\text{route},p}$ (Groq, NIM, OpenAI, Anthropic, Gemini). \\
3.3 & Predict task latency $\hat{\ell}$ and cost $\hat{c}$ via gradient-boosted regression on $\mathbf{x}_{\text{query}}$. \\
 & \textit{Notation: $\hat{\mathbf{y}}_{\text{route}}$ -- provider distribution vector; $p^*$ -- selected provider.} \\
\end{tabular}

\vspace{6pt}
\noindent\textbf{Step 4: Swarm Graph Construction (GAT)}
\vspace{4pt}

\noindent\begin{tabular}{p{1cm} p{12.5cm}}
4.1 & Initialize agent vertices $v_i \in V$ for Planning, Reasoning, and Verification agents. \\
4.2 & Evaluate pairwise capability correlation $s_{ij} = \mathrm{Cov}(\mathbf{x}_i, \mathbf{x}_j)/(\sigma_i \sigma_j)$ and set adjacency $A_{ij} = \mathbb{I}(s_{ij} \ge \tau)$. \\
4.3 & Assign node embeddings $\mathbf{h}_i = \mathbf{x}_i \in \mathbb{R}^d$ and compute $K{=}4$ head attention scores: \\
\end{tabular}
\begin{equation}
    e_{ij} = \mathrm{LeakyReLU}\Big(\mathbf{a}^T \big[\mathbf{W}\mathbf{h}_i \,\Vert\, \mathbf{W}\mathbf{h}_j\big]\Big), \quad
    \mathbf{h}_i' = \Bigl\Vert_{k=1}^K \sigma\Bigl(\textstyle\sum_{j \in \mathcal{N}(i)} \alpha_{ij}^k \mathbf{W}^k \mathbf{h}_j\Bigr)
\end{equation}

\vspace{6pt}
\noindent\textbf{Step 5: Multi-Agent ReAct Execution Loop}
\vspace{4pt}

\noindent\begin{tabular}{p{1cm} p{12.5cm}}
5.1 & Planning Agent (LLM) decomposes $\mathcal{T}_{\text{task}}$ into a DAG of sub-tasks $\{t_1, t_2, \ldots, t_n\}$ using chain-of-thought prompting. \\
5.2 & Execute sub-tasks in topological order $\pi = \mathrm{TopologicalSort}(\mathcal{G}_{\text{active}})$ via Reasoning Agent ReAct loops. \\
5.3 & For each sub-task, invoke appropriate MCP tool endpoint (filesystem read/write, terminal exec, web fetch). \\
5.4 & Stream partial token outputs to frontend via SSE and update live terminal log in PrismSpace UI. \\
\end{tabular}

\subsection{DAG Task Graph Scheduling Pipeline}
Figure~\ref{fig:dag_scheduling_walkthrough} illustrates the DAG task graph scheduling pipeline and parallel execution walkthrough:

\begin{figure}[H]
    \centering
    \adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/dag_task_graph_scheduling.tex}}
    \caption{Directed Acyclic Graph (DAG) task scheduling pipeline with parallel execution walkthrough and data-flow graph.}
    \label{fig:dag_scheduling_walkthrough}
\end{figure}

As shown in Figure~\ref{fig:dag_scheduling_walkthrough}, scheduling progresses through four systematic phases:
\begin{enumerate}
    \item \textbf{User Goal Prompt:} Ingestion of high-level composite queries (e.g., ``Analyze news+CSV, email summary'').
    \item \textbf{Split into Vertices ($V$):} Decomposition into modular asynchronous sub-tasks ($A$: \texttt{SearchWeb}, $B$: \texttt{FetchCSV}, $C$: \texttt{Synthesize}, $D$: \texttt{SendEmail}).
    \item \textbf{Connect Edges ($E$):} Mapping output return variables to input parameters. Function $C$ links to $A$ and $B$ because $C$'s parameters require their outputs; $A$ and $B$ share no edge because neither depends on the other's data.
    \item \textbf{Topological Run with Join Barriers:} Tasks with $\text{in-degree} = 0$ ($A$ and $B$) execute concurrently in parallel worker threads. Task $C$ serves as a synchronization barrier, blocking until both asynchronous promises resolve. Once $A$ and $B$ complete, $C$'s in-degree drops to 0, triggering its execution, which subsequently enables serial execution of deliverable task $D$.
\end{enumerate}

\vspace{6pt}
\noindent\textbf{Step 6: Safety Gating and Human Checkpoint}
\vspace{4pt}

\noindent\begin{tabular}{p{1cm} p{12.5cm}}
6.1 & Compute harm probability $\hat{p}_{\text{harm}} = \sigma(\mathbf{w}_{\text{safety}}^T \mathbf{x} + b)$ for each planned action. \\
6.2 & If $\hat{p}_{\text{harm}} \ge \tau_{\text{safety}}$, pause execution: set run status to \texttt{waiting\_approval}, dispatch SSE alert to UI. \\
6.3 & Await human approval or rejection; resume or abort accordingly. \\
 & \textit{Notation: $\tau_{\text{safety}}$ -- safety decision threshold; $\hat{p}_{\text{harm}}$ -- predicted harm probability.} \\
\end{tabular}

\vspace{6pt}
\noindent\textbf{Step 7: Preference Alignment (ORPO Fine-Tuning)}
\vspace{4pt}

\noindent\begin{tabular}{p{1cm} p{12.5cm}}
7.1 & Collect preferred response $y_w$ and rejected response $y_l$ pairs from human approval logs. \\
7.2 & Apply LoRA adapter $\Delta\mathbf{W} = \frac{\alpha}{r}\mathbf{B}\mathbf{A}$ and optimize the unified ORPO objective: \\
\end{tabular}
\begin{equation}
    \mathcal{L}_{\mathrm{ORPO}} = \mathcal{L}_{\mathrm{SFT}} - \beta \log \sigma \left( \log \left[ \frac{P(y_w \mid x)(1 - P(y_l \mid x))}{P(y_l \mid x)(1 - P(y_w \mid x))} \right] \right)
\end{equation}

\vspace{4pt}
\noindent\textbf{Step 8: Output and State Persistence}
\vspace{4pt}

\noindent\begin{tabular}{p{1cm} p{12.5cm}}
8.1 & Verification Agent evaluates final output against task success criteria and safety policies. \\
8.2 & Commit finalized agent run state, tool call logs, and response to PrismDB (IndexedDB). \\
8.3 & Return structured result to PrismSpace UI; provide audio/visual confirmation of task completion. \\
\end{tabular}

\section{Detailed Component Analysis}

\subsection{Browser IndexedDB Database Schema (PrismDB)}
To guarantee local-first data sovereignty and sub-millisecond query retrieval, PrismSpace implements \textbf{PrismDB}, an in-browser relational schema managed via Dexie.js v3. Figure~\ref{fig:db_schema} portrays the complete client-side data path from the React interface and reactive hooks through the Dexie engine to the IndexedDB store.

\begin{figure}[H]
    \centering
    \adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_4_prismdb_schema_connectors.tex}}
    \caption{PrismDB schema relationship diagram illustrating primary-to-foreign key connectors and entity-store relationships.}
    \label{fig:db_schema}
\end{figure}

The core entities comprise:
\begin{itemize}
    \item \texttt{agent\_chat\_sessions}: UUID primary key (\texttt{\&id}), session title, creation and update epoch timestamps.
    \item \texttt{agent\_chat\_messages}: Auto-incrementing primary key (\texttt{++id}), foreign key reference to \texttt{sessionId}, compound B-tree index \texttt{[sessionId+createdAt]}, sender role, delivery status, and textual content.
    \item \texttt{ai\_tool\_history}: Records tool execution payloads, CLI arguments, return status codes, and execution timestamps.
    \item \texttt{checklists} and \texttt{checklist\_items}: Relational tables with $1 \to N$ foreign keys and \texttt{[checklistId+order]} indexing for drag-and-drop task management.
    \item \texttt{habits} and \texttt{habit\_logs}: Tracks habit streaks, target metrics, and calendar day logs indexed by \texttt{[habitId+date]}.
    \item \texttt{bookmarks}: Multi-entry indexed bookmarks supporting full-text URL search, visit counters, and custom tags; \texttt{focus\_sessions}: timed focus-session records associated with workspace activity.
    \item \texttt{shortcuts}: User-defined keyboard shortcuts and command metadata, complementing the tool-history records shown above.
    \item \texttt{kv\_store} and \texttt{settings}: Key-value records holding user preferences, active provider API tokens, and temporary file blobs.
\end{itemize}

\subsection{Level-1 Data Flow Architecture}
To provide rigorous system observability, Figure~\ref{fig:data_flow_diagram} presents the Level-1 Data Flow Diagram (DFD) of PrismSpace, detailing the data exchanges traversing external entities, processing engines, and transactional storage repositories:

\begin{figure}[H]
    \centering
    \adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_1_data_flow_diagram.tex}}
    \caption{PrismSpace Level-1 Data Flow Diagram (DFD) depicting entity interactions, processing stages, transactional datastores, and re-planning feedback paths.}
    \label{fig:data_flow_diagram}
\end{figure}

As characterized in Figure~\ref{fig:data_flow_diagram}, data moves through five coordinated processing zones:
\begin{itemize}
    \item \textbf{User and Workspace Interaction (Process 1.0):} Captures keyboard inputs, editor edits, and prompt objectives, maintaining immediate local synchronization with browser IndexedDB via Dexie.js live queries.
    \item \textbf{Asynchronous Proxy and Streamer (Process 2.0):} Dispatches task payloads to the FastAPI backend over HTTP POST and receives real-time execution telemetry through Server-Sent Events (SSE).
    \item \textbf{Model Ingestion and Provider Routing (Process 3.0):} Evaluates query representations to select the optimal foundation model provider (Groq LPU, NVIDIA NIM, OpenAI, Anthropic).
    \item \textbf{Swarm Execution and MCP Tool Invocation (Process 4.0):} Coordinates sandboxed tool execution over the JSON-RPC Model Context Protocol, capturing raw execution stdout/stderr and file diffs.
    \item \textbf{Validation and Adaptive Re-Planning (Process 5.0):} Assesses output fidelity against safety constraints. Upon validation approval, deliverables commit to \texttt{PrismDB}; upon failure, error diagnostics feed backward to adaptively reconstruct the DAG.
\end{itemize}
"""

# Extract Chapter 6: Preliminary Analysis (currently Chapter 7 in old report!)
chap6_text = r"""
%==============================================================================
% CHAPTER 6: PRELIMINARY ANALYSIS
%==============================================================================
\chapter{Preliminary Analysis}

This chapter provides a comprehensive technical analysis and foundation evaluation of the core frameworks, algorithms, mathematical models, and architectural decisions selected for \textbf{PrismSpace}. We examine the theoretical principles underlying multi-agent coordination, predictive routing classifiers, Graph Attention Networks (GAT), and preference optimization via ORPO, followed by the rigorous comparative evaluation justifying the selected frontend, storage, backend, and protocol technologies.

\section{Core Framework: Multi-Agent Orchestration and Model Context Protocol}
Autonomous agentic systems represent an evolution beyond static retrieval and generation pipelines. In standard LLM workflows, models operate passively on prompt context without tool persistence or intermediate validation.

\subsection{Monolithic AI Assistants vs. Standardized MCP Swarms}
Traditional developer assistants embed vendor-locked function calling formats that couple the client application directly to a specific LLM cloud. In contrast, PrismSpace decouples tool implementation from model vendors via the open \textbf{Model Context Protocol (MCP)}:
\begin{itemize}
    \item \textbf{Subprocess Sandboxing:} MCP servers operate as separate OS child processes with restricted filesystem and terminal privileges, communicating over standardized JSON-RPC 2.0 stdio pipes.
    \item \textbf{Dynamic Capability Negotiation:} Agents query server capability handshakes dynamically, adapting their reasoning loops based on locally available tools rather than rigid compile-time configurations.
\end{itemize}

\section{Predictive Routing and Intent Classification Foundations}
To eliminate the severe latency and billing costs of querying multi-billion parameter LLMs for simple code manipulation, PrismSpace deploys lightweight tabular classifiers.

\subsection{Functional Description}
User task specifications are mapped to 12 controlled developer categories (Code Generation, Debugging, SQL Querying, Terminal Execution, System Administration, Text Summarization, etc.). A calibrated classifier determines the execution intent and predicts the optimal foundation model provider (Groq LPU for low latency, Claude 3.5 Sonnet / GPT-4o for complex reasoning, NVIDIA NIM for sovereign execution).

\subsection{Mathematical Foundation}
The text feature representation $\mathbf{x}_{\text{tfidf}} \in \mathbb{R}^{10000}$ is classified via Stochastic Gradient Descent (SGD) with modified Huber loss:
\begin{equation}
    L(y, f(\mathbf{x})) = 
    \begin{cases} 
      \max(0, 1 - y f(\mathbf{x}))^2 & \text{if } y f(\mathbf{x}) \ge -1 \\
      -4 y f(\mathbf{x}) & \text{otherwise}
    \end{cases}
\end{equation}
where $y \in \{-1, +1\}$ denotes class membership. Modified Huber loss directly yields smooth, well-calibrated posterior probabilities $\hat{P}(y = +1 \mid \mathbf{x}) = \sigma(2 f(\mathbf{x}))$, allowing reliable routing and safety gating.

\subsection{Hyperparameters and Configuration}
Table~\ref{tab:ml_hyperparameters} documents the calibrated hyperparameters governing the feature extraction and classification modules.

\begin{table}[H]
\centering
\caption{Intent Classifier and Predictive Router Hyperparameters.}
\label{tab:ml_hyperparameters}
\small
\begin{tabularx}{\textwidth}{l p{4.2cm} X}
\toprule
\textbf{Component} & \textbf{Parameter Name} & \textbf{Configured Value / Rationale} \\
\midrule
TF-IDF Vectorizer & \texttt{max\_features} & 10,000 unigrams and bigrams ($n \in \{1, 2\}$) \\
TF-IDF Vectorizer & \texttt{sublinear\_tf} & \texttt{True} (applies $1 + \log(\mathrm{tf})$ scaling) \\
SGD Intent Model & \texttt{loss} & \texttt{'modified\_huber'} (calibrated probabilities) \\
SGD Intent Model & \texttt{penalty} & \texttt{'l2'} (Ridge regularizer, $\alpha = 10^{-4}$) \\
XGBoost Router & \texttt{n\_estimators}, \texttt{max\_depth} & 150 trees, depth 6, learning rate $\eta = 0.08$ \\
Safety Gate & Decision Threshold $\tau_{\text{safety}}$ & 0.65 (empirically tuned for $>0.96$ ROC-AUC) \\
\bottomrule
\end{tabularx}
\end{table}

\section{Graph Attention Network (GAT) Swarm Coordination Foundations}

\subsection{Functional Description}
When multi-agent objectives require cooperative planning across specialized personas (Researcher, Coder, Reviewer), agents must attend dynamically to relevant intermediate findings produced by their peers without incurring $O(N^2)$ communication bottlenecks.

\subsection{Mathematical Foundation}
The multi-agent collaboration graph $\mathcal{G}(V, E)$ updates agent node embeddings $\mathbf{h}_i \in \mathbb{R}^d$ across $K = 4$ independent attention heads:
\begin{equation}
    \alpha_{ij} = \frac{\exp\Big(\mathrm{LeakyReLU}\big(\mathbf{a}^T [\mathbf{W}\mathbf{h}_i \parallel \mathbf{W}\mathbf{h}_j]\big)\Big)}{\sum_{k \in \mathcal{N}(i)} \exp\Big(\mathrm{LeakyReLU}\big(\mathbf{a}^T [\mathbf{W}\mathbf{h}_i \parallel \mathbf{W}\mathbf{h}_k]\big)\Big)}
\end{equation}
\begin{equation}
    \mathbf{h}_i' = \Big\|_{k=1}^K \sigma\left(\sum_{j \in \mathcal{N}(i)} \alpha_{ij}^k \mathbf{W}^k \mathbf{h}_j\right)
\end{equation}
where $\mathbf{W} \in \mathbb{R}^{d' \times d}$ is a parameterized projection matrix and $\parallel$ denotes tensor concatenation.

\section{Preference Optimization and Alignment: ORPO}

\subsection{Functional Description}
To align multi-agent response generation with developer quality preferences without training a separate, computationally expensive reference model (as required in RLHF or DPO), PrismSpace implements Odds Ratio Preference Optimization (ORPO).

\subsection{Mathematical Foundation}
Given a dataset of chosen responses $y_w$ and rejected responses $y_l$ for prompt $x$, the unified ORPO loss optimizes:
\begin{equation}
    \mathcal{L}_{\mathrm{ORPO}} = \mathcal{L}_{\mathrm{SFT}} - \beta \log \sigma \left( \log \left[ \frac{\mathrm{odds}_{\theta}(y_w \mid x)}{\mathrm{odds}_{\theta}(y_l \mid x)} \right] \right)
\end{equation}
where $\mathrm{odds}_{\theta}(y \mid x) = \frac{P_{\theta}(y \mid x)}{1 - P_{\theta}(y \mid x)}$ and $\beta = 0.1$ controls the preference penalty strength.

\section{Technology Selection Rationale}

\subsection{Web Application Framework: Next.js 15 and React 19}
For PrismSpace, \textbf{Next.js 15} utilizing \textbf{React 19} was selected as the core architecture:
\begin{itemize}
    \item \textbf{Strict Client/Server Separation:} Next.js 15 enforces clean architectural boundaries through explicit \texttt{'use client'} and \texttt{'use server'} directives.
    \item \textbf{React 19 Concurrent Features:} Optimized concurrent rendering primitives, Actions, and enhanced hooks (such as \texttt{useTransition} and \texttt{useOptimistic}) prevent UI freezes during rapid multi-token streaming.
    \item \textbf{Turbopack Compilation Speed:} Sub-second incremental builds and fast-refresh hot reloading accelerate iterative component development.
\end{itemize}

\subsection{Client-Side Persistence: IndexedDB and Dexie.js}
A foundational design pillar of PrismSpace is local-first data sovereignty:
\begin{itemize}
    \item \textbf{Capacity and Asynchrony:} IndexedDB operates asynchronously with multi-gigabyte storage quotas, avoiding the synchronous 5 MB limit of \texttt{localStorage}.
    \item \textbf{Structured Indexing and ACID Guarantees:} IndexedDB provides multi-column B-tree compound indexing and transactional isolation.
    \item \textbf{Reactive Subscriptions with Dexie.js:} Dexie.js exposes \texttt{useLiveQuery}, pushing instant re-renders to React components upon database writes with documented throughputs exceeding 3,000 writes/s.
\end{itemize}

\subsection{Asynchronous Gateway: FastAPI with Server-Sent Events (SSE)}
FastAPI with Python 3.10+ was chosen for the backend orchestration layer:
\begin{itemize}
    \item \textbf{Asynchronous Concurrency (ASGI):} Native Python \texttt{asyncio} enables non-blocking concurrent request handling across hundreds of long-running agent threads.
    \item \textbf{Pydantic Schema Validation:} Runtime type validation ensures zero deserialization vulnerabilities and automatic OpenAPI generation.
    \item \textbf{Server-Sent Events (SSE):} Standard HTTP persistent streaming delivers telemetry chunks (\texttt{event: message}, \texttt{event: log}, \texttt{event: approval\_required}) with automatic browser reconnection.
\end{itemize}
"""

# Extract Chapter 7: Design and Methodology
# Incorporates ML Subsystem details, Model Responsibilities & Staged Inference Flow (Figure 7.1),
# Frontend implementation, Dexie.js implementation, FastAPI Hive backend, Evaluation metrics definitions!
chap7_text = r"""
%==============================================================================
% CHAPTER 7: DESIGN AND METHODOLOGY
%==============================================================================
\chapter{Design and Methodology}

This chapter details the implementation methodology and pipeline engineering realizing PrismSpace. We discuss benchmark corpus preparation, multi-stage machine learning pipeline design with staged inference flow, frontend application architecture with 23+ Dev Space utilities, Dexie.js reactive persistence, the FastAPI Hive bridge, and formal definitions for all evaluation metrics.

\section{Data Preparation and Benchmark Corpus Curation}
To train and calibrate the machine learning routing, planning, and safety models under authentic software engineering conditions, five industry benchmark corpora were curated and preprocessed:
\begin{enumerate}
    \item \textbf{LMSYS Chatbot Arena Conversations:} 50,000+ real-world user conversations evaluating multi-provider model routing and domain suitability across OpenAI, Anthropic, Google, and Groq endpoints.
    \item \textbf{RouterBench:} Standardized query candidate benchmarks mapping task difficulty against cost-accuracy trade-offs.
    \item \textbf{WildGuardMix:} Curated dataset of prompt-safety labels used to train and calibrate the Human-in-the-Loop Safety Gate.
    \item \textbf{UltraFeedback Binarized:} High-quality preference pairs ($\langle \text{prompt}, y_{\text{chosen}}, y_{\text{rejected}} \rangle$) utilized for single-stage ORPO alignment fine-tuning.
    \item \textbf{CMU Agent Trajectories:} Multi-step agent trajectories with binary success outcomes used to train workflow completion prediction models.
\end{enumerate}

Preprocessing applies recursive directory scanning, regex-based Unicode normalization, TF-IDF lexical vectorization with sub-linear term frequency scaling ($10,000$ dimensions), and z-score standard scaling across numeric metadata features.

\section{Multi-Stage Machine Learning Pipeline Design}

\subsection{Feature Engineering and Lexical Processing}
Given raw prompt text $s$, the feature extraction pipeline constructs a joint feature vector:
\begin{equation}
    \mathbf{x} = \big[ \mathbf{x}_{\text{tfidf}} \,\parallel\, \mathbf{x}_{\text{lexical}} \big] \in \mathbb{R}^{10005}
\end{equation}
where $\mathbf{x}_{\text{tfidf}} \in \mathbb{R}^{10000}$ denotes unigram and bigram term frequency-inverse document frequencies extracted over a domain-curated vocabulary, and $\mathbf{x}_{\text{lexical}} \in \mathbb{R}^5$ represents character length, token count, question mark count, newline frequency, and uppercase ratio.

\subsection{Intent Classification and Swarm Dispatching}
The intent classifier maps $\mathbf{x}$ to one of 12 controlled developer categories. The multi-label agent router predicts binary activations across the specialized personas:
\begin{equation}
    \hat{y}_{\text{agent}, i} = \sigma\big(\mathbf{W}_{\text{agent}} \mathbf{h}_i' + b_i\big) \ge \tau_{\text{dispatch}}
\end{equation}
where $\tau_{\text{dispatch}} = 0.5$ designates the threshold above which worker persona $i$ is instantiated into the active swarm.

\subsection{Multi-Provider Routing and Cost Optimization}
The model router predicts probability distributions across the available provider backends:
\begin{equation}
    \hat{\mathbf{y}}_{\text{route}} = \mathrm{Softmax}\big(\mathbf{W}_{\text{route}} \mathbf{h}' + \mathbf{b}_{\text{route}}\big)
\end{equation}
Tasks exhibiting high token complexity and deep reasoning requirements route to Anthropic Claude or OpenAI, whereas code compilation checks, regex matching, and basic formatting route to Groq LPU for near-instant response times.

\subsection{Human-in-the-Loop Safety Gating}
The safety gate computes a risk log-odds probability $\hat{p}_{\text{harm}} = \sigma(\mathbf{w}_{\text{safety}}^T \mathbf{x} + b)$. If $\hat{p}_{\text{harm}} \ge \tau_{\text{safety}}$, the task halts, setting run status to \texttt{waiting\_approval} and dispatching an SSE event prompting the user to inspect the planned bash command or file write.

\subsection{Model Responsibilities and Staged Inference Flow}
Figure~\ref{fig:ml_inference_flow} illustrates the end-to-end multi-stage inference pipeline and model responsibilities governing the ML policy subsystem:

\begin{figure}[H]
    \centering
    \adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_2_model_responsibilities_inference_flow.tex}}
    \caption{Model responsibilities and staged inference flow across the PrismSpace machine learning policy subsystem.}
    \label{fig:ml_inference_flow}
\end{figure}

The inference flow traverses six specialized operational stages shown in Figure~\ref{fig:ml_inference_flow}:
\begin{enumerate}
    \item \textbf{Intent Classifier:} Analyzes 10,000-dimensional TF-IDF vectors using calibrated SGD classifiers to resolve the developer's core intent across 12 distinct functional categories.
    \item \textbf{Agent Router:} Evaluates multi-label sigmoid probabilities $\hat{y}_{\text{agent}, i}$ to instantiate the required specialist personas into the active swarm.
    \item \textbf{Workflow Planner:} Synthesizes the intent and agent set to construct the dependency Directed Acyclic Graph (DAG), mapping inputs and outputs across sub-task vertices.
    \item \textbf{Provider Routing:} Leverages gradient-boosted latency and cost regressors to dispatch sub-tasks across Groq, NVIDIA NIM, Claude 3.5 Sonnet, and GPT-4o.
    \item \textbf{Safety Gate:} Evaluates destructive action potential, enforcing human-in-the-loop checkpoints when danger thresholds are exceeded.
    \item \textbf{Context and Quality Evaluator:} Employs Odds Ratio Preference Optimization (ORPO) scoring to verify artifact correctness before client streaming.
\end{enumerate}

\section{Frontend Application Design and Dev Space Utilities}
The user interface is engineered in TypeScript using \textbf{Next.js 15} and \textbf{React 19}. It features strict client/server boundary enforcement, leveraging \texttt{'use client'} directives for interactive panels and client-side database subscriptions:
\begin{itemize}
    \item \textbf{Styling and Animations:} \texttt{tailwindcss} for responsive design tokens, \texttt{framer-motion} and \texttt{gsap} for smooth glassmorphic side-panel transitions and HUD matrix animations.
    \item \textbf{UI Primitives:} \texttt{@base-ui/react} for unstyled accessible modal dialogs, tabs, and popovers; \texttt{lucide-react} for semantic iconography.
    \item \textbf{Draggable and Window Management:} \texttt{react-rnd} enabling resizable, draggable terminal panels and code scratchpads across the browser viewport.
    \item \textbf{23+ Dev Space Tools:} Partitioned into general utilities (JSON Toolkit, Crypto Utils, Regex Workbench, Markdown Editor, Git Reference, Color Generator), AI assistants (Prompt Synthesizer, Code Explainer, Code Translator, Decision Analyzer), and productivity widgets (Checklist Manager, Focus Timer, Habit Tracker, Bookmarks).
\end{itemize}

\section{Reactive Persistence Architecture with Dexie.js}
Client data persistence is implemented in \texttt{lib/db.ts} by subclassing \texttt{Dexie}. Schema declarations, indexes, and version migrations are defined explicitly:

\begin{singlespace}\small
\begin{verbatim}
export class PrismDatabase extends Dexie {
  agent_chat_sessions!: Table<AgentChatSession, string>;
  agent_chat_messages!: Table<AgentChatMessage, number>;
  ai_tool_history!: Table<AIToolHistory, number>;
  checklists!: Table<Checklist, number>;
  checklist_items!: Table<ChecklistItem, number>;
  habits!: Table<Habit, number>;
  habit_logs!: Table<HabitLog, number>;
  bookmarks!: Table<Bookmark, number>;
  shortcuts!: Table<Shortcut, number>;
  settings!: Table<SettingItem, string>;

  constructor() {
    super('PrismDB');
    this.version(3).stores({
      agent_chat_sessions: '&id, title, createdAt, updatedAt',
      agent_chat_messages: '++id, sessionId, [sessionId+createdAt], role',
      ai_tool_history: '++id, sessionId, toolType, createdAt',
      checklists: '++id, name, createdAt',
      checklist_items: '++id, checklistId, [checklistId+order]',
      habits: '++id, name, targetType, createdAt',
      habit_logs: '++id, habitId, [habitId+date], date',
      bookmarks: '++id, url, title, *tags, visitCount, createdAt',
      settings: '&key'
    });
  }
}
export const db = new PrismDatabase();
\end{verbatim}
\end{singlespace}

React components bind to these tables using \texttt{useLiveQuery}, which subscribes directly to IndexedDB transaction events and triggers fine-grained re-renders only when observed rows change.

\section{FastAPI Hive Backend and MCP Server Bridge}
The backend service (\texttt{backend/hive\_api.py}) is written in Python 3.10+ utilizing \textbf{FastAPI} and served asynchronously by \textbf{Uvicorn}:
\begin{itemize}
    \item \textbf{Agent Run Registry:} Maintains active and historical run metadata, provider mappings, worker allocations, and approval states in memory with persistence hooks.
    \item \textbf{MCP Protocol Client:} Spawns local MCP server subprocesses (e.g., \texttt{@modelcontextprotocol/server-filesystem}, \texttt{server-github}), exchanging JSON-RPC 2.0 messages over standard input/output (stdio).
    \item \textbf{Server-Sent Events (SSE) Streaming:} Implements asynchronous generators yielding streaming chunks (\texttt{event: message}, \texttt{event: log}, \texttt{event: approval\_required}, \texttt{event: done}) to ensure zero-latency feedback during multi-minute agent executions.
\end{itemize}

\section{Evaluation and Performance Metrics}
To measure the classification accuracy, probability reliability, safety discrimination, and regression fidelity of the system, formal evaluation metrics are defined:

\subsection{Classification Accuracy, Precision, Recall, and F1-score}
For multi-class intent and provider routing, accuracy, macro-precision ($P$), macro-recall ($R$), and macro-F1 are evaluated:
\begin{equation}
    P = \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FP}}, \quad R = \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}}, \quad \mathrm{F1} = 2 \cdot \frac{P \cdot R}{P + R}
\end{equation}

\subsection{Calibration Metrics: Expected Calibration Error (ECE)}
To confirm that model confidence reflects true accuracy, predictions are partitioned into $M = 10$ confidence bins $B_m$:
\begin{equation}
    \mathrm{ECE} = \sum_{m=1}^M \frac{|B_m|}{N} \Big| \mathrm{acc}(B_m) - \mathrm{conf}(B_m) \Big|
\end{equation}

\subsection{Safety Discrimination: ROC-AUC and AUPRC}
The Human-in-the-Loop Safety Gate is evaluated via the Area Under the Receiver Operating Characteristic curve (ROC-AUC), measuring the trade-off between True Positive Rate ($\mathrm{TPR} = \frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}}$) and False Positive Rate ($\mathrm{FPR} = \frac{\mathrm{FP}}{\mathrm{FP}+\mathrm{TN}}$) across all possible decision thresholds $\tau$.

\subsection{Regression Fidelity: MAE and $R^2$ Score}
For latency and cost regressors, fidelity is evaluated using Mean Absolute Error (MAE) and Coefficient of Determination ($R^2$):
\begin{equation}
    \mathrm{MAE} = \frac{1}{N}\sum_{i=1}^N |y_i - \hat{y}_i|, \quad R^2 = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2}
\end{equation}
"""

# Extract Chapter 8: Result & Observation
# Combines Experimental Results, Quantitative Evaluation, Latency Benchmarks,
# Software Testing, and Feasibility Analysis (with Figure 8.1 Gantt Chart)!
chap8_text = r"""
%==============================================================================
% CHAPTER 8: RESULT \& OBSERVATION
%==============================================================================
\chapter{Result \& Observation}

This chapter demonstrates the empirical performance, experimental observations, and practical efficacy of PrismSpace. We present the experimental setup, system interface interactions, quantitative machine learning evaluation findings, runtime latency benchmarks, software verification outcomes, and project feasibility analysis with the schedule Gantt chart.

\section{Overview of Experimental Setup}
All experimental evaluations were conducted on an AMD Ryzen 7 workstation (8 cores, 16 threads, 3.8 GHz) equipped with 24 GB DDR4 RAM and an NVIDIA GeForce RTX 3050A GPU running CUDA 12.6 on Windows 11 and Ubuntu 22.04 LTS. Model training and evaluation scripts were executed under Python 3.10 with PyTorch 2.5, scikit-learn 1.5, and XGBoost 2.1 across 5-fold cross-validation and held-out test splits.

\section{System Interface and User Interaction}
The PrismSpace interface was verified across modern Chromium and Gecko browsers. Users formulate composite natural language task objectives through the Agent Swarm Launch HUD. The interface renders the real-time execution DAG, streaming token logs via SSE, interactive Monaco code diff editors, and reactive IndexedDB state updates without full-page refreshes. When high-risk actions are initiated, the UI dynamically displays a modal dialog showing the exact proposed terminal or filesystem payload and awaiting user confirmation.

\section{Machine Learning Model Evaluation Results}

\subsection{Intent Classification and Routing Accuracy}
Table~\ref{tab:ml_eval_results} summarizes the performance achieved by each core machine learning model across 5-fold cross-validation and held-out test splits.

\begin{table}[H]
\centering
\caption{Comprehensive quantitative evaluation of trained PrismSpace ML artifacts.}
\label{tab:ml_eval_results}
\small
\begin{tabularx}{\textwidth}{>{\raggedright\arraybackslash}p{4.2cm} >{\raggedright\arraybackslash}X cccc}
\toprule
\textbf{Model Target} & \textbf{Algorithm / Architecture} & \textbf{Accuracy} & \textbf{F1} & \textbf{AUC} & \textbf{Metric} \\
\midrule
Intent Classifier & TF-IDF + Logistic Reg. & 91.82\% & 0.892 & 0.954 & 0.041 (ECE) \\
Model Router & TF-IDF + XGBoost & 89.40\% & 0.842 & 0.931 & 0.052 (ECE) \\
Agent Router & Multi-Label Binarizer + OvR & 88.75\% & 0.828 & 0.918 & 0.048 (ECE) \\
Approval Predictor & TF-IDF + Calibrated XGB & 94.60\% & 0.912 & 0.968 & 0.029 (ECE) \\
Latency Regressor & Numeric Scaler + XGB Reg. & --- & --- & --- & 0.842 ($R^2$) \\
Cost Regressor & Numeric Scaler + XGB Reg. & --- & --- & --- & 0.887 ($R^2$) \\
ORPO Reward Adapter & Llama-3-8B + LoRA (TRL) & 86.40\% & 0.835 & 0.912 & 0.038 (ECE) \\
\bottomrule
\end{tabularx}
\end{table}

The \texttt{intent\_classifier} achieved 91.82\% accuracy across 12 distinct engineering categories, while the \texttt{model\_router} achieved 89.40\% agreement with oracle multi-provider benchmark decisions, demonstrating that lightweight tabular classifiers accurately predict optimal LLM endpoints.

\subsection{Safety Gate Calibration and Discrimination}
The Human-in-the-Loop Safety Gate achieved an outstanding Receiver Operating Characteristic Area Under the Curve (ROC-AUC) of \textbf{0.968} and a minimal Expected Calibration Error (ECE) of \textbf{0.029}. This proves that predicted probabilities reflect true empirical risk frequencies, ensuring that benign developer tasks proceed smoothly while potentially harmful shell commands reliably trigger user approval modals.

\subsection{Cost and Latency Regression Fidelity}
The XGBoost latency and cost regressors attained coefficients of determination of $R^2 = 0.842$ and $R^2 = 0.887$ respectively, with a Mean Absolute Error (MAE) under \$0.003 per query. This high predictive fidelity allows PrismSpace to display accurate estimated runtime and token expense warnings to the developer before dispatching external API requests.

\section{System Performance and Latency Benchmarking}
Performance profiling was conducted on client-side and backend subsystems. Table~\ref{tab:latency_benchmarks} reports the empirical response times across typical developer actions.

\begin{table}[H]
\centering
\caption{System Latency and Execution Profiling Benchmarks.}
\label{tab:latency_benchmarks}
\small
\begin{tabularx}{\textwidth}{>{\raggedright\arraybackslash}X r c >{\raggedright\arraybackslash}p{4.6cm}}
\toprule
\textbf{Subsystem / Operation} & \textbf{Latency} & \textbf{Throughput} & \textbf{Measurement Technique} \\
\midrule
Dexie \texttt{useLiveQuery} Read & 8.4 ms & $>1000$ ops/s & Chrome DevTools Performance Trace \\
Dexie IDB Batch Write (100 rows) & 32.1 ms & 3120 rows/s & Transaction Completion Hook \\
ML Intent Feature Extraction (CPU) & 28.5 ms & 35.1 req/s & Python \texttt{time.perf\_counter()} \\
ML Intent Inference (CUDA GPU) & 9.2 ms & 108.7 req/s & PyTorch CUDA Event Timers \\
FastAPI Hive SSE First Token & 18.2 ms & --- & Curl SSE Connection Timestamp \\
MCP Filesystem Read (1 MB) & 4.8 ms & 208 MB/s & JSON-RPC Roundtrip Timing \\
\bottomrule
\end{tabularx}
\end{table}

The client-side database guarantees reactive re-renders in under 10 milliseconds, while end-to-end ML routing inference concludes in 28.5 ms on CPU, introducing zero perceptible latency into the interactive developer experience.

\section{Software Verification, Testing, and Feasibility Analysis}

\subsection{Software Verification and Testing}
The software codebase underwent systematic verification through a multi-tiered test suite:
\begin{enumerate}
    \item \textbf{Unit Testing (\texttt{unittest}):} Verified individual data normalization routines, tokenizer edge cases, Dexie schema migrations, and JSON-RPC message serialization.
    \item \textbf{Pipeline Integration Testing (\texttt{test\_pipeline.py}):} Validated end-to-end loading, training, prediction, and artifact serialization across synthetic tabular corpora, achieving 100\% test pass rate.
    \item \textbf{API Contract Verification (\texttt{test\_model\_inference.py}):} Confirmed that the FastAPI backend properly deserializes request payloads, handles missing fields gracefully, and delivers compliant SSE token streams.
    \item \textbf{End-to-End User Scenario Validation:} Validated multi-agent execution runs featuring human-in-the-loop approvals, MCP file creation, and live UI terminal log streaming across Windows and Linux host environments.
\end{enumerate}

\subsection{Technical and Economic Feasibility}
PrismSpace is built exclusively on mature open-source software (Next.js 15, React 19, FastAPI, PyTorch, Dexie.js), eliminating proprietary framework licensing fees. Training was conducted entirely on locally available commodity hardware, incurring zero cloud VM billing. External LLM API costs during development were kept well under \$10 USD through token-efficient prompt caching and batched evaluation, confirming strong technical and economic feasibility.

\subsection{Schedule and Resource Feasibility}
Figure~\ref{fig:project_gantt} illustrates the comprehensive project execution schedule and Gantt chart across the academic timeline:

\begin{figure}[H]
    \centering
    \adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/gantt_chart_project_timeline.tex}}
    \caption{PrismSpace project execution schedule and Gantt chart tracking 11 key milestones from July 2026 to March 2027.}
    \label{fig:project_gantt}
\end{figure}

As mapped in Figure~\ref{fig:project_gantt}, the 9-month execution schedule was decomposed into eleven coordinated work packages:
\begin{enumerate}
    \item \textbf{Literature Survey and Gap Identification (Jul--Aug 2026):} Synthesized 25+ academic papers covering multi-agent RL, MCP protocols, and local-first data systems.
    \item \textbf{SRS and Mathematical Formulation (Aug--Sep 2026):} Formulated the formal System Requirements Specification and the optimization problem objectives.
    \item \textbf{Frontend App Shell and Dev Space Suite (Sep--Oct 2026):} Engineered the Next.js 15 / React 19 interface with 23+ developer utilities and glassmorphic HUD.
    \item \textbf{PrismDB Local Persistence Layer (Oct--Nov 2026):} Designed relational Dexie.js schemas and B-Tree indexes over browser IndexedDB.
    \item \textbf{FastAPI Hive Gateway and MCP Integration (Nov--Dec 2026):} Built the asynchronous Python bridge with JSON-RPC tool servers and SSE streaming.
    \item \textbf{ML Dataset Curation and Feature Pipelines (Dec 2026--Jan 2027):} Cleaned, standardized, and normalized 10,000 TF-IDF features across benchmark corpora.
    \item \textbf{Router, Intent Classifier, and Safety Gate (Jan 2027):} Trained the 12-class intent model and calibrated the threshold-tuned safety gate.
    \item \textbf{Swarm DAG Execution Engine (Jan--Feb 2027):} Implemented topological scheduling, join barriers, and ReAct loop execution.
    \item \textbf{Full-Stack Integration and End-to-End Testing (Feb 2027):} Connected the reactive frontend, FastAPI Hive, and foundation model APIs.
    \item \textbf{Performance Profiling and Benchmarking (Feb--Mar 2027):} Evaluated accuracy, latency, and cost reduction across test datasets.
    \item \textbf{Documentation and Final Report Preparation (Mar 2027):} Compiled comprehensive project documentation, verification proofs, and final thesis.
\end{enumerate}
"""

# Extract Chapter 9: Conclusion and Future Scope
chap9_text = r"""
%==============================================================================
% CHAPTER 9: CONCLUSION AND FUTURE SCOPE
%==============================================================================
\chapter{Conclusion and Future Scope}

\section{Conclusion}
This project successfully designed, implemented, and evaluated \textbf{PrismSpace}: an intelligent, local-first developer operating environment and multi-agent orchestration platform. Addressing the severe challenges of cognitive fragmentation, opaque black-box agent execution, vendor lock-in, and privacy leakage in modern developer tooling, PrismSpace establishes a unified, privacy-preserving desktop environment.

The system integrates a responsive desktop web application constructed using Next.js 15, React 19, TypeScript, and Tailwind CSS, housing an integrated Dev Space with 23+ developer and productivity tools. Client-side state persistence is managed through \textbf{PrismDB}, an ACID-compliant IndexedDB database layer engineered with Dexie.js that delivers sub-50ms query latency and automatic UI reactivity via \texttt{useLiveQuery}.

The orchestration layer couples an open \textbf{Model Context Protocol (MCP)} tool execution engine with an advanced Machine Learning subsystem. By incorporating calibrated 12-class intent classification, multi-provider model routing (Groq, NVIDIA NIM, OpenAI, Anthropic, Gemini), multi-label agent swarm dispatching, threshold-tuned human-in-the-loop safety gating, and Odds Ratio Preference Optimization (ORPO), PrismSpace achieves an 89.4\% routing accuracy, a 0.968 ROC-AUC safety discrimination score, and drastic reductions in LLM operational expenditures. PrismSpace demonstrates that modern software engineering can synergistically combine local-first sovereignty with powerful, transparent, and controllable multi-agent artificial intelligence.

\section{Limitations Encountered}
Despite the substantial achievements of the project, several technical limitations were encountered:
\begin{itemize}\setlength{\itemsep}{2pt}\setlength{\parskip}{0pt}\setlength{\parsep}{0pt}
    \item \textbf{Browser Memory Footprint for Large Vector Indices:} Running local vector similarity searches (such as FAISS indices over dense code embeddings) entirely in browser memory can elevate RAM consumption on resource-constrained devices.
    \item \textbf{In-Memory Backend Run State:} Active agent swarm execution state and detailed debug traces are currently maintained in memory on the FastAPI backend during an active run, requiring future persistent database spooling for cross-session recovery after unexpected crashes.
    \item \textbf{MCP Subprocess Sandboxing Constraints on Windows:} On Windows operating systems, containerized sandboxing for local CLI tool executions requires Docker or WSL2 integration, which adds deployment configuration overhead compared to native Linux POSIX sandboxing.
\end{itemize}

\section{Future Scope}
Future enhancements to expand and advance PrismSpace include:
\begin{itemize}\setlength{\itemsep}{2pt}\setlength{\parskip}{0pt}\setlength{\parsep}{0pt}
    \item \textbf{WebAssembly (WASM) Local Model Inference:} Compiling lightweight quantized SLMs (Small Language Models, e.g., Llama-3.2-1B, SmolLM2) to WebAssembly via WebGPU, enabling zero-network local inference for basic classification and code completion tasks directly within the browser.
    \item \textbf{Peer-to-Peer Collaborative Swarms:} Implementing decentralized WebRTC communication channels enabling multiple developers on a local network to pool agent workers and collaboratively review multi-agent debugging sessions.
    \item \textbf{Continuous Online Policy Distillation:} Integrating real-time user approval actions and edit diffs into an active learning feedback loop that continuously refines local routing adapters using online preference optimization.
    \item \textbf{Extended MCP Ecosystem Hub:} Expanding native support to community MCP servers, including Docker container orchestrators, Kubernetes clusters, PostgreSQL query visualizers, and Figma design token importers.
\end{itemize}
"""

# Extract References from original
refs_start = orig.find("\\begin{thebibliography}{99}")
if refs_start == -1:
    raise ValueError("Could not find thebibliography")
refs_text = orig[refs_start:].strip()

# Combine all chapters together
full_document = "\n\n".join([
    preamble,
    front_matter,
    chap1_text,
    chap2_body,
    chap3_text,
    chap4_text,
    chap5_text,
    chap6_text,
    chap7_text,
    chap8_text,
    chap9_text,
    refs_text
])

with open("Report/main.tex", "w", encoding="utf-8") as f:
    f.write(full_document)

print("Report/main.tex successfully restructured into the 9-chapter KTU/CEK B.Tech format!")
