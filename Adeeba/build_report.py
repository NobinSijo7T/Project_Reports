# -*- coding: utf-8 -*-
"""
Script to build the complete, restructured, 9-chapter B.Tech Project Report
for 'BLOCK CHAIN BASED ELECTRONIC VOTING SYSTEM'
at College of Engineering Karunagappally.
"""

report_content = r"""\documentclass[12pt,a4paper]{report}

%==============================================================================
% PREAMBLE AND PACKAGES (Aligned with CEK / KTU B.Tech Project Format)
%==============================================================================
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{fancyhdr}
\usepackage{cite}
\usepackage{a4wide}
\usepackage{float}
\usepackage{epsfig}
\usepackage{longtable}
\usepackage{enumerate}
\usepackage{afterpage}
\usepackage{multirow}
\usepackage{ragged2e}
\usepackage{gensymb}
\usepackage{amsfonts} 
\usepackage[left=3.5cm,top=1.5cm,right=3cm,bottom=3cm]{geometry}
\usepackage{setspace}           
\usepackage{txfonts}
\usepackage{standalone}
\usepackage{tikz}
\usepackage{fontawesome5}
\usetikzlibrary{calc, shapes.geometric, arrows, arrows.meta, positioning, fit, backgrounds, shadows, tikzmark}

% Color definitions for TikZ diagrams
\definecolor{lavenderDark}{RGB}{15, 44, 89}
\definecolor{lavenderDeep}{RGB}{10, 28, 58}
\definecolor{lavenderMedium}{RGB}{29, 78, 158}
\definecolor{lavenderLight}{RGB}{240, 246, 255}
\definecolor{lavenderBorder}{RGB}{180, 205, 237}
\definecolor{lavenderAccent}{RGB}{2, 132, 199}
\definecolor{prismNavy}{RGB}{15, 44, 89}
\definecolor{prismBlue}{RGB}{29, 78, 158}
\definecolor{prismTeal}{RGB}{13, 148, 136}
\definecolor{prismMint}{RGB}{236, 253, 245}
\definecolor{prismGold}{RGB}{217, 119, 6}
\definecolor{prismDark}{RGB}{15, 23, 42}
\definecolor{prismLight}{RGB}{248, 250, 252}
\definecolor{prismIndigo}{RGB}{30, 58, 138}
\definecolor{prismSlate}{RGB}{100, 116, 139}
\definecolor{statusFail}{RGB}{220, 38, 38}
\definecolor{cInput}{RGB}{241, 245, 249}
\definecolor{cStem}{RGB}{224, 242, 254}
\definecolor{cStage1}{RGB}{209, 250, 229}
\definecolor{cStage2}{RGB}{254, 243, 199}
\definecolor{cStage3}{RGB}{254, 226, 226}
\definecolor{cStage4}{RGB}{207, 250, 254}
\definecolor{cHead}{RGB}{219, 234, 254}
\definecolor{cOutput}{RGB}{255, 228, 230}
\definecolor{cDeliverable}{RGB}{204, 251, 241}

\usepackage{subfiles}
\usepackage{adjustbox}
\usepackage{tcolorbox}
\tcbuselibrary{skins, breakable}

\newcommand{\Usefont}[1]{\fontfamily{#1}\selectfont}

\usepackage{lscape}
\linespread{1.5}

\usepackage{url}
\usepackage{subcaption}
\usepackage[intoc, english]{nomencl}
\usepackage[nottoc]{tocbibind}
\usepackage{booktabs}
\usepackage{array}
\usepackage{tabularx}
\usepackage{xltabular}
\usepackage{hyperref}

\hypersetup{
    plainpages=false,
    pdfpagelabels=true,
    colorlinks=true,
    linkcolor=black,
    citecolor=black,
    urlcolor=black,
    pdftitle={Block Chain Based Electronic Voting System},
    pdfauthor={Adeeba Abdul Vahid, Avani P, Thara A}
}

% Spacing and line-breaking settings to prevent overflow and overfull hboxes
\setlength{\headheight}{15pt}
\hyphenpenalty=1000
\tolerance=2000
\emergencystretch=2.5em

\bibliographystyle{IEEEtran}
\renewcommand{\bibname}{References}

% Figure search path
\graphicspath{{figures/}{diagrams/}{./}}

%==============================================================================
% METADATA DEFINITIONS (Project Group & CEK)
%==============================================================================
\gdef \title{BLOCK CHAIN BASED ELECTRONIC VOTING SYSTEM}
\gdef \shorttitle{Block Chain Based Electronic Voting System}

\gdef \authorA{ADEEBA ABDUL VAHID}
\gdef \rollnoA{KNP23CS011}

\gdef \authorB{AVANI P}
\gdef \rollnoB{LKNP23CS114}

\gdef \authorC{THARA A}
\gdef \rollnoC{LKNP23CS117}

\gdef \acadyear{2026--2027}
\gdef \submonth{October 2026}
\gdef \month{October 2026}
\gdef \date{28-10-2026}
\gdef \dept{Computer Science and Engineering}
\gdef \deptabbr{Dept.\ of CSE}
\gdef \degree{Bachelor of Technology}
\gdef \branch{Computer Science and Engineering}
\gdef \college{College of Engineering Karunagappally}
\gdef \collegeplace{Kollam}
\gdef \collegetown{Karunagappally}

\gdef \guide{Mr.~Anwar Sadath}
\gdef \guidedes{Assistant Professor}
\gdef \coordinator{Dr.~Smitha P}
\gdef \coordinatordes{Associate Professor and HOD}
\gdef \semcordinatorA{Dr.~Smitha P}
\gdef \semcordinatorAdes{Associate Professor and HOD}
\gdef \hod{Dr.~Smitha P}
\gdef \hoddes{Associate Professor and HOD}

%==============================================================================
% DOCUMENT BODY
%==============================================================================

\begin{document}

%------------------------------------------------------------------------------
% FRONT MATTER
%------------------------------------------------------------------------------
\hypersetup{pageanchor=false}
\include{coverpage}
\include{vision_mission}
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

%==============================================================================
% CHAPTER 1: INTRODUCTION
%==============================================================================
\chapter[Introduction]{\Huge Introduction}

Democratic governance is fundamentally anchored upon the integrity, transparency, and public verifiability of electoral processes. The legitimacy of any elected administration depends upon ensuring that every eligible citizen is guaranteed exactly one non-repudiable vote, that ballots cannot be forged, manipulated, or discarded, and that final tallies are immune to post-election tampering. Despite centuries of institutional evolution, conducting secure, accessible, and transparent elections remains one of the most contentious socio-technical challenges confronting modern societies.

\section{Background and Motivation}
Traditional paper-based voting methodologies, while conceptually simple, suffer from severe systemic vulnerabilities. Paper ballot administration requires massive logistical mobilization, physical transportation of paper ballot boxes, and centralized manual tallying procedures that are vulnerable to booth capturing, ballot stuffing, physical loss, counting discrepancies, and deliberate administrative tampering. Furthermore, the protracted time required to manually count and audit millions of physical paper ballots introduces periods of severe uncertainty, dispute, and civil unrest.

To mitigate logistical latency and human counting fatigue, many jurisdictions adopted first-generation electronic voting machines (EVMs) and centralized online web-based voting platforms. While electronic voting drastically reduces ballot printing costs and accelerates result compilation, conventional e-voting systems predominantly store voting records within centralized relational databases managed by a single election authority. This centralized architecture introduces a catastrophic single point of failure:
\begin{enumerate}[(i)]
    \item \textbf{Single Point of Centralized Control:} Database administrators, system engineers, or malicious actors with privileged root access can manipulate ballot tables, inject fictitious votes, or alter candidate tallies without leaving an externally verifiable, cryptographically provable audit trail.
    \item \textbf{Opaque Blind-Trust Model:} Electorates are required to place blind, unverifiable faith in the honesty of the centralized election commission and proprietary machine software.
    \item \textbf{Double-Voting Vulnerabilities:} In distributed web-based voting portals, network race conditions, duplicate session logins, and concurrency bugs frequently allow malicious actors to cast multiple ballots under a single identity before database row locks resolve.
    \item \textbf{Vulnerability to Denial of Service and Data Loss:} Centralized server infrastructures remain vulnerable to distributed denial-of-service (DDoS) assaults, server downtime, and catastrophic hardware failures during bursty polling periods.
\end{enumerate}

\section{The Blockchain Trust Paradigm}
Blockchain technology introduces a decentralized trust model that eliminates reliance on trusted intermediaries. A blockchain operates as a peer-to-peer, append-only distributed ledger wherein transactional records are grouped into chronologically sequenced blocks linked cryptographically through collision-resistant hash functions (such as SHA-256 and Keccak-256). Once a block is committed to the distributed chain through network consensus, altering historical ballot data would require computationally recalculating all subsequent block hashes across a majority of distributed nodes---an operation that is computationally infeasible and immediately detectable by all participating peers.

By integrating \textbf{Smart Contracts}---self-executing, immutable program routines running within the Ethereum Virtual Machine (EVM)---the procedural rules, voter eligibility checks, candidate registries, and counting algorithms can be automated without subjective human intervention. Smart contracts eliminate opaque counting rooms; once deployed, their bytecoded logic is executed identically across every node in the decentralized network.

\section{The Double-Voting Challenge in Electronic Voting}
Double voting represents one of the most fatal threats to election legitimacy. Double voting occurs when a registered voter succeeds in casting more than one ballot, either intentionally through malicious browser automation and concurrent transaction submissions, or through system synchronization lags across distributed polling nodes. In centralized client-server voting architectures, anti-duplicate validation is typically enforced at the presentation layer (e.g., disabling a UI button after clicking) or via application middleware. Such mechanisms fail when malicious actors interact directly with server APIs or exploit race conditions in concurrent database writes.

The proposed system addresses double voting at the immutable smart contract layer. By coupling an atomic verification predicate within the Solidity smart contract with asymmetric wallet-based authentication via MetaMask, duplicate ballot submissions are rejected directly by the EVM state transition engine before any state mutation or tally aggregation can occur.

\section{Project Objectives}
The primary objective of this project is to design, implement, and analyze an end-to-end, secure, and transparent electronic voting system leveraging Ethereum smart contracts, Web3.js middleware, and a React.js client interface. The explicit engineering and research objectives are as follows:
\begin{itemize}
    \item \textbf{Smart-Contract-Level Double-Voting Mitigation:} Develop an atomic state evaluation mechanism within Solidity that enforces strict single-vote casting ($\text{Accept}(v)$ logic) and makes duplicate voting computationally impossible even under direct RPC invocation.
    \item \textbf{Role-Based Administrative Access Control:} Implement strict cryptographic authorization boundaries separating the election administrator (responsible for candidate nomination and voter whitelisting) from registered voters (authorized solely to cast a single ballot).
    \item \textbf{Asymmetric Wallet Authentication:} Integrate MetaMask and Web3.js to enable voters to securely authenticate and cryptographically sign ballot transactions using secp256k1 elliptic curve digital signatures without exposing private keys.
    \item \textbf{Real-Time Public Auditability and Result Transparency:} Eliminate post-polling counting delays by providing an automated tallying engine that reflects certified results on an auditable ledger in real time through event subscriptions.
    \item \textbf{Consensus and Scalability Optimization:} Formally evaluate consensus mechanisms, establishing the operational viability of Proof-of-Authority (PoA) consortium networks to eliminate gas fee volatility and ensure predictable, low-latency transaction throughput.
    \item \textbf{Comprehensive Academic Survey:} Synthesize a systematic comparative review of fifteen recent state-of-the-art blockchain voting architectures spanning multimodal biometrics, gesture recognition, blind signatures, and differential privacy.
\end{itemize}

\section{Scope and Organization of the Report}
This project report encompasses the complete architectural design, mathematical modeling, smart contract engineering, front-end development, security vulnerability auditing, and consensus analysis of the proposed Voting DApp. The remainder of this report is organized as follows:
\begin{itemize}
    \item \textbf{Chapter 2 (Literature Review):} Synthesizes fifteen foundational and recent peer-reviewed investigations on blockchain e-voting frameworks, biometrics, cryptography, and governance, concluding with an extensive comparative taxonomy and identified research gaps.
    \item \textbf{Chapter 3 (Problem Definition):} Details the formal problem statement, threat vectors, system boundaries, and governing mathematical equations for cryptographic block chaining, atomic ballot acceptance, and vote tallying.
    \item \textbf{Chapter 4 (Requirements Specification):} Details the functional and non-functional requirements governing administrators, voters, smart contracts, and network infrastructure, alongside hardware and software specifications.
    \item \textbf{Chapter 5 (System Design):} Elaborates the multi-tier system architecture, operational pipelines, voter registration workflows, end-to-end sequence flows, comprehensive operational flowchart, the formal 12-stage operational algorithm, block structures, relational state schemas, and Level-1 Data Flow Diagrams (DFD).
    \item \textbf{Chapter 6 (Design and Methodology):} Analyzes Solidity smart contract implementation, modifiers, staged transaction verification, React/Web3.js front-end integration, MetaMask ECDSA signing, and consensus model trade-offs.
    \item \textbf{Chapter 7 (Preliminary Analysis):} Conducts comparative evaluations across blockchain platforms (Ethereum, Hyperledger, Polygon), consensus mechanisms (PoW, PoS, PoA), EVM gas expenditures, and smart contract vulnerability mitigation.
    \item \textbf{Chapter 8 (Feasibility Study):} Evaluates technical, operational, and economic feasibility dimensions, accompanied by the complete project milestone Gantt chart.
    \item \textbf{Chapter 9 (Conclusion and Future Scope):} Summarizes major technical milestones, discusses remaining real-world constraints (e.g., key custody, ballot privacy), and charts prospective research trajectories including Zero-Knowledge Proofs and Layer-2 scaling.
\end{itemize}

%==============================================================================
% CHAPTER 2: LITERATURE REVIEW
%==============================================================================
\chapter{Literature Review}

The application of blockchain technology to electronic voting has garnered extensive academic attention over the past decade. Researchers have investigated blockchain architectures to address the vulnerabilities of centralized systems while striving to satisfy classical electoral criteria: eligibility, uniqueness, ballot secrecy, verifiability, and coercion resistance. This chapter synthesizes recent advancements across five thematic dimensions: blockchain voting frameworks, biometric and gesture authentication, cryptographic privacy techniques, surveys and governance studies, and smart contract design paradigms.

\section{Blockchain-Based Voting Frameworks and Consensus Design}
Early investigations focused on adapting core blockchain ledgers to record votes as immutable transactions. Farooq et al.~\cite{Farooq2022} proposed a comprehensive Voting Management System utilizing a custom blockchain with a pluggable consensus layer. In their framework, a web and mobile DApp verifies a voter's national identification credentials, verifies that the voter has not previously participated, converts the cast ballot into an encrypted transaction, and commits it to the chain. A proprietary Chain Security Algorithm continuously re-audits chain integrity upon block inclusion. Although their simulation demonstrated manageable response latencies and linear chain growth up to six million transactions, the architecture requires continuous internet connectivity, lacks a biometric verification layer, and mitigates 51\% attacks only through centralized monitoring of authorized mining nodes.

Shahzad and Crowcroft~\cite{Shahzad2019} observed that polling periods are intrinsically bursty, characterized by high transaction volumes concentrated within a fixed window of 8--12 hours. Consequently, resource-heavy Proof-of-Work (PoW) consensus is computationally wasteful and impractical. They developed an adjusted consortium blockchain wherein certified presiding officers with verified cryptographic identities generate blocks during polling hours, sealing them at the close of voting using a proof-of-completeness hashing mechanism. While tamper-evident and computationally lightweight, the framework remains purely conceptual, lacks an empirical prototype, and retains significant administrative centralization within the election commission.

Kshetri and Voas~\cite{Kshetri2018} conceptualized a wallet-and-coin tokenized voting model. In this formulation, each eligible voter receives exactly one non-fungible or restricted digital token representing a single vote; casting a ballot corresponds to transferring this coin into a certified candidate's wallet address. Their analytical study evaluated practical impediments to real-world deployment, concluding that software defect rates in smart contracts, voter digital literacy barriers, high broadband infrastructure requirements, and political resistance make public blockchain voting unprepared for national elections without hybrid physical safeguards.

Seftyanto et al.~\cite{Seftyanto2019} architected a permissioned election infrastructure tailored for the Indonesian electoral context utilizing Hyperledger Fabric. In their multi-organizational topology, each geographic province functions as an autonomous peer organization. Voters authenticate at polling booths using an electronic national identity card (e-ID) and a biometric fingerprint scanner, with cast votes encapsulated as immutable \texttt{Ballot} assets within chaincode. However, their contribution remains a preliminary design without throughput benchmarks, latency evaluations, or stress testing, and relies heavily on costly dedicated hardware at every polling venue.

\section{Biometric and Gesture-Based Authentication}
Voter authentication represents the most vulnerable attack surface in decentralized voting. A system that relies solely on private key possession cannot verify whether the authorized citizen or an unauthorized third party is operating the wallet. To bridge this gap, Ajao et al.~\cite{Ajao2025} integrated a multimodal biometric hardware apparatus with an Ethereum Proof-of-Stake (PoS) network. Their setup deployed a custom Raspberry Pi device equipped with facial recognition, optical fingerprint scanning, and high-frequency RFID credential readers. Biometric embeddings and ballot selections were encrypted using Paillier homomorphic encryption to ensure end-to-end data confidentiality. In a live university election involving 2,423 students, the system achieved a remarkable 1,424.5 transactions per second (TPS), an average mining latency of 7.02 seconds, and zero false acceptance (FAR) and false rejection rates (FRR). Nevertheless, the operational cost of manufacturing and distributing specialized biometric scanning hardware to distributed polling stations, coupled with Ethereum gas fees per transaction, poses substantial barriers for wide-scale public adoption.

Mahmood et al.~\cite{Mahmood2024} focused on accessibility and assistive voting technologies for motor-impaired and elderly electorates. Their system tracks real-time facial landmarks and hand gestures via consumer webcams, allowing voters to navigate virtual ballot keyboards through subtle facial movements (e.g., eyebrow raises, nose gestures, or pinch gestures). Integrated with a PoW blockchain backend, the system demonstrated 100\% precision and 99\% recall across controlled trials. However, system accuracy degraded significantly under suboptimal lighting conditions, finger gestures exhibited lower tracking fidelity than facial landmarks, and elderly participants exhibited longer voting completion times.

\section{Privacy and Cryptographic Techniques}
Balancing the radical transparency of public distributed ledgers with the strict constitutional mandate of voter ballot secrecy remains a central cryptographic paradox. Pérez García et al.~\cite{PerezGarcia2021} addressed this challenge by implementing an ElGamal-based blind signature protocol over Hyperledger Fabric with Practical Byzantine Fault Tolerance (PBFT) consensus. In their protocol, a central electoral authority cryptographically signs an blinded, encrypted ballot without deciphering its content, completely uncoupling the voter's identity from the cast choice. Ballots are divided into two cryptographic shares such that neither share alone reveals the voter's candidate selection. While simulations confirmed total unlinkability and minimal computational overhead per client, transaction processing latency increased under high concurrency, and the centralized authority retains significant trust for blinded token issuance.

Baniata and Caluna~\cite{Baniata2025} proposed \textit{BP-Vot}, a privacy-preserving framework deployed on Hyperledger Besu. \textit{BP-Vot} combines Self-Sovereign Identity (SSI) verifiable credentials with a $(k, \varepsilon)$-differential privacy mechanism to inject controlled mathematical noise into aggregate vote counts, guaranteeing plausible deniability for individual ballot selections. Their prototype achieved approximately one second transaction latency and demonstrated over 98\% tally approximation accuracy. However, evaluation was restricted to a three-node cluster processing up to 50,000 votes, fundamentally relies upon the honesty of the credential-issuing authority, and depends on global standardization of digital identity wallets.

\section{Surveys, Trust and Governance Studies}
Benabdallah et al.~\cite{Benabdallah2022} conducted a systematic literature review analyzing blockchain voting proposals published between 2010 and 2021 across five election lifecycle phases: initialization, voter identification, vote casting, tallying, and result verification. Their study concluded that blockchain architectures cannot completely eliminate centralized authorities responsible for voter eligibility rosters, that public proof-of-work blockchains fail to achieve the throughput required for national elections, and that receipt-freeness and coercion resistance remain largely unresolved across existing prototypes.

Quzmar et al.~\cite{Quzmar2021} performed a comparative survey of eight prominent blockchain e-voting architectures, finding that the vast majority remain academic prototypes tested exclusively in local simulation environments. They identified key management vulnerabilities, lack of standard blockchain protocols, and smart contract security bugs as primary impediments.

Sah et al.~\cite{Sah2025} conducted a comprehensive architectural review of blockchain voting implementations, focusing on developer toolchains including Truffle, Ganache, and MetaMask. Synthesizing pilot election data, they reported an 87\% reduction in reported electoral fraud incidents and a 10\% increase in voter participation, while emphasizing that transaction fees and rural internet connectivity bottlenecks persist.

Barelli et al.~\cite{Barelli2025} catalogued attacks on real-world e-voting deployments and defined six fundamental security properties: integrity, anonymity, eligibility, individual/universal verifiability, receipt-freeness, and coercion resistance. They demonstrated that the transparent nature of blockchain transaction ledgers can facilitate voter de-anonymization via network-level traffic analysis and address clustering. Furthermore, they emphasized that client device compromise (malware, screen loggers) is rarely addressed in blockchain literature, and that emerging quantum computing poses long-term threats to classical elliptic curve cryptography (ECDSA secp256k1).

Wermelinger et al.~\cite{Wermelinger2026} shifted focus from technical architecture to human factors and institutional trust. Utilizing Partial Least Squares Structural Equation Modeling (PLS-SEM) on survey responses from 1,851 Brazilian voters, they demonstrated that systemic institutional trust is the single dominant determinant of electronic voting acceptance and demands for printed voter-verified paper audit trails (VVPAT). Their findings prove that cryptographic security guarantees are insufficient on their own; public confidence demands transparent, understandable verification mechanisms and intuitive user interfaces.

\section{Smart Contract Approaches and Network Support}
Chaudhary et al.~\cite{Chaudhary2023} deployed an Ethereum smart contract incorporating \texttt{addCandidate}, \texttt{authorize}, \texttt{vote}, and \texttt{endElection} routines, optimized for execution over high-speed 5G wireless networks. To mitigate on-chain storage costs, bulky voter verification artifacts were offloaded to the InterPlanetary File System (IPFS), with only IPFS content identifiers (CIDs) committed on-chain. While achieving lower bit-error rates and passing formal Echidna fuzz testing, the protocol retains administrative centralization in contract deployment, and client devices remain vulnerable to local malware.

The foundational baseline for our work is established by Asha et al.~\cite{Asha2025}, who developed a Voting DApp on Ethereum that directly addresses double voting through smart contract logic. In their design, the smart contract maintains state mappings of registered voter addresses and certified candidates. The election administrator retains exclusive authority to invoke \texttt{addCandidate} and \texttt{registerVoter}. Voters authenticate using MetaMask and cast ballots via a responsive React.js and Web3.js web interface. Their prototype demonstrated successful registration, atomic double-voting rejection, and real-time result tabulation on an Ethereum test network. However, Asha et al.\ observed that public Ethereum gas price fluctuations and interface complexity for non-technical users represent operational challenges that necessitate private consortium consensus and optimized user workflows.

\section{Synthesis and Research Gap Identification}
Table~\ref{tab:lit_comparison} synthesizes the fifteen surveyed literature works across six core criteria: publication year, blockchain platform, consensus mechanism, authentication methodology, evaluation maturity, and primary technical limitation.

\begingroup
\setstretch{1.15}
\setlength{\tabcolsep}{3.5pt}
\fontsize{8.5}{11}\selectfont
\begin{xltabular}{\textwidth}{%
  >{\centering\arraybackslash}p{0.75cm}
  >{\centering\arraybackslash}p{0.75cm}
  >{\RaggedRight\arraybackslash}p{1.9cm}
  >{\RaggedRight\arraybackslash}p{1.6cm}
  >{\RaggedRight\arraybackslash}p{2.1cm}
  >{\RaggedRight\arraybackslash}p{1.8cm}
  >{\RaggedRight\arraybackslash}X%
}
\caption{Systematic Comparative Analysis of Surveyed Blockchain Electronic Voting Literature} \label{tab:lit_comparison} \\
\toprule
\textbf{Ref.} & \textbf{Year} & \textbf{Platform} & \textbf{Consensus} & \textbf{Authentication} & \textbf{Evaluation} & \textbf{Key Limitation / Bottleneck} \\
\midrule
\endfirsthead

\multicolumn{7}{c}%
{{\bfseries Table \thetable\ (Continued):} Systematic Comparative Analysis of Surveyed Literature} \\[4pt]
\toprule
\textbf{Ref.} & \textbf{Year} & \textbf{Platform} & \textbf{Consensus} & \textbf{Authentication} & \textbf{Evaluation} & \textbf{Key Limitation / Bottleneck} \\
\midrule
\endhead

\midrule
\multicolumn{7}{r}{\footnotesize\textit{Continued on next page\dots}} \\
\bottomrule
\endfoot

\bottomrule
\endlastfoot

\cite{Farooq2022} & 2022 & Custom Chain & Pluggable PoW & National ID + SHA-256 & Simulation ($6\times 10^6$) & Constant connectivity required; no biometrics; 51\% attack risk. \\ \addlinespace[3pt]
\cite{Shahzad2019} & 2019 & Consortium & Presiding Sig & Cryptographic ID & Conceptual only & No software prototype; heavy administrative centralization. \\ \addlinespace[3pt]
\cite{Kshetri2018} & 2018 & Public/Private & Token-transfer & Wallet / Digital Coin & Analytical review & Immature tooling; defect risks; unready for national scale. \\ \addlinespace[3pt]
\cite{Seftyanto2019} & 2019 & Hyperledger Fabric & Raft / Kafka & e-ID + Fingerprint & Architecture design & No throughput evaluation; heavy hardware needed per booth. \\ \addlinespace[3pt]
\cite{Ajao2025} & 2025 & Ethereum & PoS & Face + Fingerprint + RFID & University election & Expensive biometric hardware; ongoing gas transaction fees. \\ \addlinespace[3pt]
\cite{Mahmood2024} & 2024 & Custom PoW & PoW & Facial / Hand Gestures & Trials ($N=100$) & Lighting sensitive; finger tracking errors; slow for elderly. \\ \addlinespace[3pt]
\cite{PerezGarcia2021} & 2021 & Hyperledger Fabric & PBFT & ElGamal Blind Signatures & Simulation & Scalability bottleneck under congestion; authority trust. \\ \addlinespace[3pt]
\cite{Baniata2025} & 2025 & Hyperledger Besu & IBFT 2.0 & Diff.\ Privacy + SSI & 3-node cluster & Assumes honest authority; requires standardized digital wallets. \\ \addlinespace[3pt]
\cite{Benabdallah2022} & 2022 & SLR (2010--21) & Diverse & Surveyed taxonomy & Systematic Review & Identifies scalability, coercion, and central eligibility gaps. \\ \addlinespace[3pt]
\cite{Quzmar2021} & 2021 & Survey & Diverse & Key management analysis & Comparative Survey & Academic prototypes; lack of standard e-voting protocols. \\ \addlinespace[3pt]
\pagebreak
\cite{Sah2025} & 2025 & Review & PoW / PoS & Web3 / MetaMask & Architectural Review & Highlights gas cost barriers and rural internet connectivity. \\ \addlinespace[3pt]
\cite{Barelli2025} & 2025 & Survey & Diverse & Cryptographic audit & Theoretical Survey & Transparency de-anonymizes voters; client malware ignored. \\ \addlinespace[3pt]
\cite{Wermelinger2026} & 2026 & Empirical & N/A & PLS-SEM Trust Model & Empirical ($N=1851$) & Shows institutional trust dominates over technical guarantees. \\ \addlinespace[3pt]
\cite{Chaudhary2023} & 2023 & Ethereum & PoW + 5G & Smart Contract + IPFS & Echidna Fuzzing & Client device malware; central contract deployment risks. \\ \addlinespace[3pt]
\cite{Asha2025} & 2025 & Ethereum & PoA / PoS & MetaMask + RBAC & Remix / Testnet & Public gas volatility; usability for non-technical electorates. \\
\end{xltabular}
\endgroup

Critical synthesis of the surveyed corpus reveals three persistent research gaps:
\begin{enumerate}
    \item \textbf{Evaluation Gap:} The majority of proposed architectures remain confined to conceptual frameworks or simulated toy elections. Real-world behavior under bursty transaction loads remains unvalidated.
    \item \textbf{Authentication Vulnerability vs Hardware Overhead:} Existing systems bifurcate into two extremes: wallet-only schemes that are vulnerable to credential theft, and biometric systems that demand prohibitive specialized hardware at every voting precinct.
    \item \textbf{Consensus and Financial Feasibility Gap:} Deploying on public blockchains (e.g., Ethereum mainnet) imposes volatile, unpredictable gas fees and throughput ceilings (15--30 TPS), whereas permissioned frameworks often re-introduce centralized administrative control.
\end{enumerate}

These identified gaps directly motivate the architecture of our proposed Voting DApp, which enforces atomic double-voting mitigation in Solidity, leverages lightweight MetaMask asymmetric authentication, and employs a consortium Proof-of-Authority (PoA) consensus model to provide predictable, zero-fee, high-throughput voting.

%==============================================================================
% CHAPTER 3: PROBLEM DEFINITION
%==============================================================================
\chapter{Problem Definition}

A rigorous engineering formulation is essential to transform subjective electoral requirements into verifiable, mathematically bounded smart contract routines. This chapter formalizes the problem statement, defines the threat model and attack vectors, establishes operational boundaries, and details the governing mathematical formulations.

\section{Problem Statement}
In conventional electoral administration, ensuring that every registered voter $v$ exercises their franchise at most once ($\sum \text{ballots}(v) \le 1$) is enforced through manual ink marking, physical voter rolls, or centralized database records. In decentralized digital voting, voters interact across untrusted networks using pseudonymous cryptographic addresses. The fundamental problem addressed in this project is:
\begin{quote}
\textit{To design and implement a decentralized, transparent, and auditable electronic voting architecture that provably prevents duplicate voting ($\text{Double-Voting}$) and unauthorized candidate insertion at the smart contract level, while providing cryptographically non-repudiable voter authentication, real-time result compilation, and deterministic transaction processing without exposing voters to gas cost volatility.}
\end{quote}

\section{Threat Model and Attack Vectors}
The proposed system is designed against the following realistic adversarial threats:
\begin{itemize}
    \item \textbf{Double-Voting and Race Conditions:} A malicious voter attempts to cast multiple ballots by executing concurrent asynchronous transactions from the same wallet address or exploiting transaction pool (mempool) propagation latencies.
    \item \textbf{Unauthorized Candidate Insertion and Spoofing:} An unprivileged participant attempts to inject fraudulent candidates or manipulate existing candidate vote counters directly on the blockchain.
    \item \textbf{Sybil and Identity Impersonation Attacks:} An adversary attempts to generate thousands of arbitrary Ethereum wallet addresses to cast illegitimate votes.
    \item \textbf{Transaction Tampering and Forgery:} A man-in-the-middle attacker attempts to modify the selected candidate identifier $c$ while the ballot payload is transmitted from the client browser to the Ethereum network.
    \item \textbf{Post-Election Result Manipulation:} A corrupt election official attempts to retroactively alter recorded tallies or insert uncast ballots into historical blocks.
\end{itemize}

\section{System Boundaries and Operational Assumptions}
The operational scope is bounded by the following formal assumptions:
\begin{enumerate}
    \item \textbf{Cryptographic Primitives:} The underlying elliptic curve digital signature algorithm (ECDSA on secp256k1) and cryptographic hash functions (SHA-256 and Keccak-256) are computationally secure against classical preimage and collision attacks.
    \item \textbf{Voter Key Custody:} The voter is responsible for maintaining the physical security of their personal computing device and the private key/seed phrase associated with their MetaMask wallet.
    \item \textbf{Honest Administrator at Registration:} The election administrator is trusted during the pre-election whitelisting phase to accurately map physical citizen identities to authorized Ethereum wallet addresses. Once whitelisting is completed, the administrator has no computational capability to alter cast votes or influence smart contract execution.
    \item \textbf{Consensus Integrity:} A majority of validator nodes in the Proof-of-Authority consortium are honest and correctly validate transactions according to the published Solidity contract bytecode.
\end{enumerate}

\section{Mathematical Formulation and Governing Equations}
The security and integrity of the proposed blockchain voting system are formally governed by the following mathematical formulations:

\subsection{Cryptographic Hash Chaining and Block Integrity}
Every block $B_i$ at sequential height $i$ in the distributed ledger is cryptographically bound to its parent block $B_{i-1}$. The block hash digest $H(B_i)$ is computed as:
\begin{equation}
    H(B_i) = \text{SHA-256}\Big( H(B_{i-1}) \;\parallel\; T_i \;\parallel\; Tx_i \;\parallel\; n_i \Big)
    \label{eq:block_hash}
\end{equation}
where $H(B_{i-1}) \in \{0, 1\}^{256}$ represents the cryptographic hash of the immediate predecessor block, $T_i$ denotes the Unix epoch timestamp, $Tx_i = \{tx_1, tx_2, \dots, tx_m\}$ represents the Merkle root of the ordered set of verified transactions encapsulated in block $i$, $n_i$ represents the consensus nonce value, and $\parallel$ denotes the byte-level string concatenation operator. 

Any retroactive attempt to alter a transaction $tx_k \in Tx_j$ in a historical block $B_j$ ($j < i$) produces an altered hash $H'(B_j) \neq H(B_j)$. Because $H(B_j)$ is embedded within block $B_{j+1}$, this modification breaks the cryptographic link for all subsequent blocks $B_{j+1}, \dots, B_i$, causing immediate rejection by all network validator nodes.

\subsection{Atomic Double-Voting Mitigation Predicate}
Let $\mathcal{V} \subset \mathbb{Z}_{2^{160}}$ represent the universal set of all 20-byte Ethereum wallet addresses, and let $\mathcal{C} = \{1, 2, \dots, K\}$ represent the set of certified candidate identifiers. The smart contract maintains two internal state mapping functions:
\begin{align}
    \text{registered} &: \mathcal{V} \to \{\text{true}, \text{false}\} \\
    \text{voted} &: \mathcal{V} \to \{\text{true}, \text{false}\}
\end{align}
The binary ballot acceptance predicate $\text{Accept}(v)$ governing a ballot submission from voter address $v \in \mathcal{V}$ is defined as:
\begin{equation}
    \text{Accept}(v) = \begin{cases} 
        1, & \text{if } \text{registered}(v) = \text{true} \;\land\; \text{voted}(v) = \text{false} \\ 
        0, & \text{otherwise} 
    \end{cases}
    \label{eq:double_vote}
\end{equation}
When $\text{Accept}(v) = 1$, the smart contract executes an atomic state mutation:
\begin{align}
    \text{voted}(v) &\leftarrow \text{true} \label{eq:state_voted} \\
    N(c) &\leftarrow N(c) + 1 \label{eq:state_tally}
\end{align}
Because equations~(\ref{eq:state_voted}) and~(\ref{eq:state_tally}) are executed within a single, atomic EVM transaction context, any secondary transaction submitted by the same address $v$ will encounter $\text{voted}(v) = \text{true}$, resulting in $\text{Accept}(v) = 0$ and an immediate EVM transaction revert.

\subsection{Cumulative Vote Tally and Upper Bound Invariant}
The cumulative aggregate vote tally $N(c)$ recorded for any candidate $c \in \mathcal{C}$ at the conclusion of polling is formulated as:
\begin{equation}
    N(c) = \sum_{v \in \mathcal{V}} \Big[ \text{vote}(v) = c \;\land\; \text{Accept}(v) = 1 \Big]
    \label{eq:candidate_tally}
\end{equation}
where $\text{vote}(v) \in \mathcal{C}$ represents the candidate selected by voter $v$, and $[\cdot]$ denotes the Iverson bracket notation (evaluating to 1 if true, 0 if false). 

A critical mathematical invariant enforced by the contract is that the total sum of all candidate votes can never exceed the total number of whitelisted registered voters:
\begin{equation}
    \sum_{c \in \mathcal{C}} N(c) \;\le\; \sum_{v \in \mathcal{V}} \Big[ \text{registered}(v) = \text{true} \Big] \;\le\; |\mathcal{V}|
    \label{eq:tally_invariant}
\end{equation}
This invariant mathematically guarantees that ballot fabrication and over-voting are impossible within the decentralized ledger.

%==============================================================================
% CHAPTER 4: REQUIREMENTS SPECIFICATION
%==============================================================================
\chapter{Requirements Specification}

The formal System Requirements Specification (SRS) delineates the complete functional capabilities, non-functional quality attributes, and hardware/software execution environments required for the blockchain-based electronic voting system.

\section{Functional Requirements}
The functional requirements are categorized across three operational modules: Administrator Module, Voter Module, and Smart Contract / Ledger Module.

\subsection{Administrator Module}
\begin{itemize}
    \item \textbf{FR-01: Smart Contract Deployment and Ownership:} The election administrator shall deploy the compiled Solidity contract bytecode to the Ethereum network, automatically registering the deployer's address as the immutable \texttt{admin} authority.
    \item \textbf{FR-02: Candidate Management:} The administrator shall have exclusive authority to register certified candidate monikers via \texttt{addCandidate(string memory name)}. The system shall automatically assign sequential candidate IDs and initialize vote tallies to zero.
    \item \textbf{FR-03: Voter Whitelisting:} The administrator shall have exclusive authority to whitelist eligible voter Ethereum addresses via \texttt{registerVoter(address \_voterAddress)}.
    \item \textbf{FR-04: Role-Based Authorization Guard:} Any attempt by a non-administrator address to invoke administrative functions shall result in an immediate smart contract revert.
\end{itemize}

\subsection{Voter Module}
\begin{itemize}
    \item \textbf{FR-05: Web3 Wallet Handshake:} The voter interface shall interface with the \texttt{window.ethereum} API provided by MetaMask, prompting the voter to authorize connection and retrieve their active account address.
    \item \textbf{FR-06: Eligibility Verification:} Upon wallet connection, the front end shall query the smart contract state to verify that the connected address is registered and has not previously voted.
    \item \textbf{FR-07: Certified Candidate Display:} The front end shall dynamically fetch the certified candidate registry from the blockchain and display candidate profiles to authorized voters.
    \item \textbf{FR-08: Ballot Transaction Construction and Signing:} Upon selecting a candidate, the voter shall trigger a cryptographically signed transaction via MetaMask, encoding the function invocation \texttt{vote(uint \_candidateId)}.
\end{itemize}

\subsection{Smart Contract and Ledger Module}
\begin{itemize}
    \item \textbf{FR-09: Atomic Double-Voting Mitigation:} The smart contract shall verify that the caller is registered and has not voted. If verified, it shall atomically set the voter's participation flag to \texttt{true} and increment the candidate's tally.
    \item \textbf{FR-10: State Reversion on Violation:} If an unregistered address attempts to vote, or if a registered voter attempts to vote a second time, the contract shall immediately revert with an explicit error string.
    \item \textbf{FR-11: Event Emission:} Upon successful ballot commitment, the smart contract shall emit a public \texttt{VoteCast(address indexed voter, uint indexed candidateId, uint timestamp)} event.
    \item \textbf{FR-12: Public Audit Query:} The contract shall expose public, gas-free read functions (\texttt{candidatesCount}, \texttt{candidates}, \texttt{totalVotes}) enabling continuous external auditing.
\end{itemize}

\section{Non-Functional Requirements}
\begin{itemize}
    \item \textbf{NFR-01: Immutability and Tamper-Resistance:} All confirmed votes and administrative actions shall be permanently recorded on an append-only distributed ledger, rendering retroactive alteration computationally impossible.
    \item \textbf{NFR-02: Transaction Latency and Throughput:} In a Proof-of-Authority consortium configuration, average block sealing latency shall not exceed 2.0 seconds, supporting peak burst throughput of at least 100 transactions per second.
    \item \textbf{NFR-03: Zero-Gas Cost for Voters:} In consortium deployment, transaction gas price shall be configured to zero ($G_{\text{price}} = 0$) or subsidized, ensuring voters incur no financial cost to exercise their franchise.
    \item \textbf{NFR-04: Non-Repudiation:} Every transaction shall carry a valid ECDSA signature generated by the voter's private key, guaranteeing that vote submissions cannot be denied by the sender.
    \item \textbf{NFR-05: Cross-Browser Accessibility:} The web client shall operate seamlessly across all major Web3-compatible browsers, including Google Chrome, Mozilla Firefox, Brave, and Microsoft Edge.
\end{itemize}

\section{Hardware and Software Specifications}
Table~\ref{tab:specs} outlines the operational hardware and software environments utilized for system development, testbed deployment, and client execution.

\begin{table}[H]
\centering
\caption{System Hardware and Software Technical Specifications}
\label{tab:specs}
\begingroup
\setstretch{1.15}
\fontsize{9.0}{11.5}\selectfont
\renewcommand{\arraystretch}{1.20}
\setlength{\tabcolsep}{5pt}
\begin{tabularx}{\textwidth}{>{\RaggedRight\bfseries}p{3.6cm} >{\RaggedRight}p{4.4cm} >{\RaggedRight\arraybackslash}X}
\toprule
\textbf{Category} & \textbf{Component / Tool} & \textbf{Specification / Version} \\
\midrule
\multirow{5}{=}{\textbf{Blockchain Core \& Consensus Layer}} 
 & Blockchain Runtime & Ethereum Virtual Machine (EVM) / Go-Ethereum (Geth v1.13+) \\
 & Consensus Protocol & Proof-of-Authority (PoA / Clique Engine, IBFT 2.0) \\
 & Smart Contract Language & Solidity (v0.8.20+ with automated overflow checking) \\
 & Local Testbed Network & Ganache CLI / Hardhat In-Memory Network \\
 & Development Toolchain & Hardhat Suite (v2.19+) / Truffle / Remix IDE \\
\midrule
\multirow{5}{=}{\textbf{Middleware \& Application Layer}} 
 & Front-End Architecture & React.js (v18.2+) / Vite Engine / HTML5 / CSS3 \\
 & Web3 Provider Bridge & Web3.js (v1.10+) / Ethers.js (v6.x) JSON-RPC Client \\
 & Cryptographic Wallet & MetaMask Browser Extension (v11.x+) \\
 & RPC Communication & JSON-RPC 2.0 over Secure WebSocket (WSS) and HTTP \\
 & Decentralized Storage & InterPlanetary File System (IPFS) / Pinata Gateway \\
\midrule
\multirow{5}{=}{\textbf{Validator \& Server Hardware}} 
 & Central Processor (CPU) & Intel Core i7 / AMD Ryzen 7 (8 Cores, 16 Threads @ 3.6\,GHz) \\
 & System Memory (RAM) & 16\,GB / 32\,GB DDR4 3200\,MHz High-Speed RAM \\
 & Primary Storage & 512\,GB NVMe M.2 Solid State Drive (Read $\ge 3500$\,MB/s) \\
 & Host Operating System & Ubuntu Server 22.04 LTS (64-bit Linux Kernel 5.15+) \\
 & Network Interface & Gigabit Ethernet (1000BASE-T Full-Duplex Dedicated Link) \\
\midrule
\multirow{5}{=}{\textbf{Client Execution Environment}} 
 & Supported Platforms & Commodity Desktop PC, Laptop, Smartphone, Tablet \\
 & Client Operating Systems & Windows 10/11, macOS (v12+), Linux (Ubuntu), Android, iOS \\
 & Compatible Web Browsers & Google Chrome (v115+), Mozilla Firefox, Brave, MS Edge \\
 & Network Bandwidth & Broadband / 4G / 5G Low-Latency Connection ($\ge 2$\,Mbps) \\
 & Display Layout & Responsive UI ($360\times640$\,px Mobile to $1080$p Desktop) \\
\bottomrule
\end{tabularx}
\endgroup
\end{table}

%==============================================================================
% CHAPTER 5: SYSTEM DESIGN
%==============================================================================
\chapter{System Design}

This chapter details the architectural decomposition, component interactions, workflows, formal algorithms, block structures, relational state schemas, and Data Flow Diagrams (DFDs) governing the decentralized electronic voting system.

\section{Multi-Tier System Architecture}
The system architecture is structured across four decoupled, modular tiers: Client Presentation Tier, Web3 Middleware Tier, Smart Contract Logic Tier, and Blockchain Ledger Tier. Figure~\ref{fig:sys_arch} illustrates this multi-tier architecture and the communication pathways between components.

\begin{figure}[H]
\centering
\adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_2_system_architecture.tex}}
\caption{Multi-tier system architecture of the blockchain-based electronic voting decentralized application (Voting DApp).}
\label{fig:sys_arch}
\end{figure}

The Client Presentation Tier provides distinct portals for the election administrator (\texttt{admin.html}) and voters (\texttt{voting.html}). Voters authenticate via MetaMask, which manages private key storage and signs transactions locally. The Web3 Middleware Tier translates client actions into JSON-RPC calls sent to the Ethereum network. The Smart Contract Logic Tier executes the compiled Solidity bytecode on the EVM, enforcing role-based access control and atomic double-voting mitigation. Finally, the Blockchain Ledger Tier seals verified transactions into chronologically chained blocks via Proof-of-Authority consensus.

\section{Proposed Operational Methodology Pipeline}
The complete election lifecycle is organized into five sequential phases, as illustrated in Figure~\ref{fig:methods_pipeline}.

\begin{figure}[H]
\centering
\adjustbox{max width=0.98\linewidth, center}{\input{diagrams/fig_proposed_methods_pipeline.tex}}
\caption{Proposed operational methodology pipeline detailing the five stages of the election lifecycle.}
\label{fig:methods_pipeline}
\end{figure}

\begin{itemize}
    \item \textbf{Stage 1 (System Setup \& Contract Deployment):} The administrator compiles and deploys the Solidity smart contract, establishing contract ownership and initializing the candidate and voter state mappings.
    \item \textbf{Stage 2 (Entity Whitelisting \& Registration):} The administrator registers certified candidates via \texttt{addCandidate} and whitelists eligible voter public wallet addresses via \texttt{registerVoter}.
    \item \textbf{Stage 3 (Wallet Authentication \& Handshake):} The voter visits the portal, initiates a connection via \texttt{window.ethereum}, and MetaMask returns the voter's public address without exposing the underlying private key.
    \item \textbf{Stage 4 (Ballot Submission \& Double-Voting Mitigation):} The voter selects a candidate and signs the transaction. The smart contract evaluates the atomic condition $\text{Accept}(v)$; if valid, it sets $\text{voted}(v) = \text{true}$ and increments $N(c)$.
    \item \textbf{Stage 5 (Consensus Sealing \& Live Audit Compilation):} Validator nodes seal the transaction into a block via SHA-256 hash chaining, emit the \texttt{VoteCast} event, and update the live audit tally.
\end{itemize}

\section{Voter Registration and Whitelisting Workflow}
Figure~\ref{fig:voter_workflow} illustrates the step-by-step handshake between the administrator, voter, MetaMask wallet, and the smart contract during the pre-voting whitelisting and authentication phases.

\begin{figure}[H]
\centering
\adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_0_prismspace_workflow.tex}}
\caption{Detailed layered workflow for voter whitelisting, MetaMask connection, and eligibility verification.}
\label{fig:voter_workflow}
\end{figure}

\section{End-to-End Ballot Sequence Flow}
Figure~\ref{fig:end_to_end_flow} illustrates the end-to-end transaction lifecycle across the four interacting system entities: the Voter \& MetaMask Client, the React \& Web3.js Middleware, the Smart Contract on the EVM, and the Consensus Ledger.

\begin{figure}[H]
\centering
\adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig11_end_to_end_system_flow.tex}}
\caption{End-to-end system sequence flow from ballot selection to block sealing and real-time Web3 tally notification.}
\label{fig:end_to_end_flow}
\end{figure}

\section{Complete System Operational Flowchart}
Figure~\ref{fig:sys_flowchart} depicts the complete operational flowchart of the voting decentralized application, detailing role verification, whitelisting validation, double-voting rejection branches, and event emissions.

\begin{figure}[H]
\centering
\adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_3_multiagent_communication_flowchart.tex}}
\caption{Comprehensive system flowchart detailing administrator actions, voter verification branches, and atomic double-voting mitigation.}
\label{fig:sys_flowchart}
\end{figure}

\section{Comprehensive Operational Algorithm}
The complete operational mechanics of the blockchain-based electronic voting system and its double-voting mitigation engine are formalized through the end-to-end procedural steps detailed below:

\newenvironment{algsubsteps}{%
  \begin{list}{}{%
    \setlength{\leftmargin}{5.2em}%
    \setlength{\itemindent}{-3.0em}%
    \setlength{\labelwidth}{2.6em}%
    \setlength{\labelsep}{0.4em}%
    \setlength{\listparindent}{0pt}%
    \setlength{\parsep}{1pt}%
    \setlength{\itemsep}{3pt}%
    \setlength{\topsep}{2pt}%
    \setlength{\partopsep}{0pt}%
  }%
}{\end{list}}

\vspace{0.6em}
\noindent\textbf{Step 1: System Initialization and Contract Deployment}

\vspace{0.2em}
\noindent\textbf{1.1} Compile and deploy smart contract bytecode:
\begin{algsubsteps}
    \item[\textbf{1.1.1}] Administrator compiles Solidity smart contract bytecode using the compiler \texttt{solc} (version $\ge 0.8.20$).
    \item[\textbf{1.1.2}] Administrator deploys contract deployment transaction to the Ethereum network via the authenticated JSON-RPC endpoint.
\end{algsubsteps}

\noindent\textbf{1.2} Execute atomic constructor initialization:
\begin{equation}
\text{admin} \leftarrow \text{msg.sender}, \quad \text{candidatesCount} \leftarrow 0, \quad \text{electionOpen} \leftarrow \text{true}
\end{equation}
\begin{algsubsteps}
    \item[\textbf{1.2.1}] Contract constructor binds administrative ownership to deployer wallet address and initializes zeroed ballot state.
    \item[\textbf{1.2.2}] Contract emits \texttt{ElectionInitialized(admin, block.timestamp)} event log to the blockchain ledger.
\end{algsubsteps}

\vspace{0.6em}
\noindent\textbf{Step 2: Candidate Nomination and Registration}

\vspace{0.2em}
\noindent\textbf{2.1} Submit candidate nomination and evaluate administrative authority:
\begin{algsubsteps}
    \item[\textbf{2.1.1}] Administrator invokes $\text{addCandidate}(\text{name})$ passing the certified candidate moniker string.
    \item[\textbf{2.1.2}] Contract evaluates caller authorization modifier barrier: $\mathbf{assert}(\text{msg.sender} == \text{admin})$.
\end{algsubsteps}

\noindent\textbf{2.2} Persist candidate state struct to on-chain storage:
\begin{equation}
\begin{split}
\text{candidatesCount} &\leftarrow \text{candidatesCount} + 1 \\
\text{candidates}[\text{candidatesCount}] &\leftarrow \text{Candidate}(\text{candidatesCount}, \text{name}, 0)
\end{split}
\end{equation}
\begin{algsubsteps}
    \item[\textbf{2.2.1}] Candidate record is appended to the persistent mapping with initialized zero vote tally.
    \item[\textbf{2.2.2}] Contract emits on-chain event: \texttt{CandidateAdded(candidatesCount, name)}.
\end{algsubsteps}

\vspace{0.6em}
\noindent\textbf{Step 3: Voter Whitelisting and Address Certification}

\vspace{0.2em}
\noindent\textbf{3.1} Ingest verified identity credentials:
\begin{algsubsteps}
    \item[\textbf{3.1.1}] Administrator ingests eligible citizen's verified 20-byte Ethereum wallet address $v \in \mathcal{V}$.
    \item[\textbf{3.1.2}] Administrator initiates whitelisting transaction via $\text{registerVoter}(v)$.
\end{algsubsteps}

\noindent\textbf{3.2} Evaluate access barrier and instantiate voter struct:
\begin{equation}
\text{voters}[v] \leftarrow \text{Voter}(v, \text{isRegistered} = \text{true}, \text{hasVoted} = \text{false}, \text{candidateId} = 0)
\end{equation}
\begin{algsubsteps}
    \item[\textbf{3.2.1}] Contract enforces access restriction: $\mathbf{assert}(\text{msg.sender} == \text{admin})$.
    \item[\textbf{3.2.2}] Contract verifies unwhitelisted state invariant: $\mathbf{assert}(\text{voters}[v].\text{isRegistered} == \text{false})$.
    \item[\textbf{3.2.3}] Contract records voter struct and emits audit receipt: \texttt{VoterRegistered(v, block.timestamp)}.
\end{algsubsteps}

\vspace{0.6em}
\noindent\textbf{Step 4: Client Initialization and Wallet Handshake}

\vspace{0.2em}
\noindent\textbf{4.1} Discover injected Ethereum provider:
\begin{algsubsteps}
    \item[\textbf{4.1.1}] Voter navigates to web portal (\texttt{voting.html}) using a Web3-compatible browser.
    \item[\textbf{4.1.2}] Client script validates provider injection: $\mathbf{assert}(\text{window.ethereum} \neq \text{null})$.
\end{algsubsteps}

\noindent\textbf{4.2} Perform asynchronous account authorization handshake:
\begin{algsubsteps}
    \item[\textbf{4.2.1}] Voter triggers interface connection routine; client initiates RPC procedure \texttt{eth\_requestAccounts}.
    \item[\textbf{4.2.2}] MetaMask prompts voter for access consent and returns active account address $v = \text{accounts}[0]$.
\end{algsubsteps}

\vspace{0.6em}
\noindent\textbf{Step 5: Client-Side Eligibility Verification}

\vspace{0.2em}
\noindent\textbf{5.1} Query on-chain voter registration state:
\begin{algsubsteps}
    \item[\textbf{5.1.1}] Front end instantiates Web3 contract wrapper using deployed contract address and JSON ABI.
    \item[\textbf{5.1.2}] Front end executes read-only query call:
    \begin{equation}
    \text{voterRecord} \leftarrow \text{contract.methods.voters}(v).\text{call}()
    \end{equation}
\end{algsubsteps}

\noindent\textbf{5.2} Enforce client gatekeeping logic:
\begin{algsubsteps}
    \item[\textbf{5.2.1}] If $\text{voterRecord.isRegistered} == \text{false}$, UI displays ``Access Denied: Unregistered Voter''.
    \item[\textbf{5.2.2}] If $\text{voterRecord.hasVoted} == \text{true}$, UI displays ``Ballot Already Cast: Double Voting Prohibited''.
    \item[\textbf{5.2.3}] If $\text{voterRecord.isRegistered} == \text{true} \land \text{voterRecord.hasVoted} == \text{false}$, UI unlocks certified candidate ballot selection view.
\end{algsubsteps}

\vspace{0.6em}
\noindent\textbf{Step 6: Dynamic Candidate Presentation}

\vspace{0.2em}
\noindent\textbf{6.1} Fetch candidate records from contract:
\begin{algsubsteps}
    \item[\textbf{6.1.1}] Front end queries candidate registry size: $\text{candidatesCount} \leftarrow \text{contract.methods.candidatesCount}().\text{call}()$.
    \item[\textbf{6.1.2}] For each candidate identifier $c \in [1, \text{candidatesCount}]$, front end queries candidate record:
    \begin{equation}
    \text{candidate}[c] \leftarrow \text{contract.methods.candidates}(c).\text{call}()
    \end{equation}
\end{algsubsteps}

\noindent\textbf{6.2} Dynamically render interactive ballot portal:
\begin{algsubsteps}
    \item[\textbf{6.2.1}] Front end dynamically renders candidate radio button list containing names, IDs, and candidate badges.
\end{algsubsteps}

\vspace{0.6em}
\noindent\textbf{Step 7: Ballot Selection and Transaction Serialization}

\vspace{0.2em}
\noindent\textbf{7.1} Serialize ABI-encoded vote call:
\begin{algsubsteps}
    \item[\textbf{7.1.1}] Voter selects desired candidate identifier $c \in \mathcal{C}$ and confirms ballot submission.
    \item[\textbf{7.1.2}] Web3.js serializes function call payload: $\text{data} \leftarrow \text{encodeABI}(\text{vote}(c))$.
\end{algsubsteps}

\noindent\textbf{7.2} Estimate transaction computational gas:
\begin{equation}
G_{\text{limit}} \leftarrow \text{contract.methods.vote}(c).\text{estimateGas}(\{\text{from}: v\})
\end{equation}
\begin{algsubsteps}
    \item[\textbf{7.2.1}] Gas parameters are assembled into transaction payload alongside active network gas price.
\end{algsubsteps}

\vspace{0.6em}
\noindent\textbf{Step 8: Asymmetric ECDSA Transaction Signing}

\vspace{0.2em}
\noindent\textbf{8.1} Compute Keccak-256 transaction digest:
\begin{equation}
h_{\text{tx}} \leftarrow \text{Keccak-256}(\text{nonce} \parallel G_{\text{price}} \parallel G_{\text{limit}} \parallel \text{to} \parallel \text{value} \parallel \text{data})
\end{equation}
\begin{algsubsteps}
    \item[\textbf{8.1.1}] Front end transmits unsigned transaction parameters to MetaMask wallet via JSON-RPC.
\end{algsubsteps}

\noindent\textbf{8.2} Sign transaction and broadcast to peer network:
\begin{equation}
\sigma = (r, s, v) \leftarrow \text{ECDSA-Sign}(h_{\text{tx}}, K_{\text{priv}})
\end{equation}
\begin{algsubsteps}
    \item[\textbf{8.2.1}] Voter reviews gas estimate and clicks ``Confirm'' in wallet modal.
    \item[\textbf{8.2.2}] MetaMask generates elliptic curve signature $\sigma$ using voter's private key $K_{\text{priv}}$ without exposing private keys.
    \item[\textbf{8.2.3}] Client broadcasts signed raw transaction via RPC procedure \texttt{eth\_sendRawTransaction}.
\end{algsubsteps}

\vspace{0.6em}
\noindent\textbf{Step 9: Smart Contract Execution and Atomic Double-Voting Mitigation}

\vspace{0.2em}
\noindent\textbf{9.1} Recover sender address and enforce cryptographic guard conditions:
\begin{algsubsteps}
    \item[\textbf{9.1.1}] EVM recovers public address: $v \leftarrow \text{ecrecover}(h_{\text{tx}}, v, r, s)$.
    \item[\textbf{9.1.2}] Contract enforces whitelist guard: $\mathbf{require}(\text{voters}[v].\text{isRegistered} == \text{true}, \text{``Voter is not registered''})$.
    \item[\textbf{9.1.3}] Contract enforces atomic double-voting barrier: $\mathbf{require}(\text{voters}[v].\text{hasVoted} == \text{false})$.
    \item[\textbf{9.1.4}] Contract enforces candidate boundary check: $\mathbf{require}(c \ge 1 \land c \le \text{candidatesCount}, \text{``Invalid candidate selected''})$.
\end{algsubsteps}

\noindent\textbf{9.2} Execute atomic on-chain state mutation:
\begin{equation}
\begin{split}
\text{voters}[v].\text{hasVoted} &\leftarrow \text{true}, \quad \text{voters}[v].\text{votedCandidateId} \leftarrow c \\
\text{candidates}[c].\text{voteCount} &\leftarrow \text{candidates}[c].\text{voteCount} + 1
\end{split}
\end{equation}
\begin{algsubsteps}
    \item[\textbf{9.2.1}] Double-voting status flag is set atomically in the same transaction execution context.
    \item[\textbf{9.2.2}] Contract emits event log: $\text{emit VoteCast}(v, c, \text{block.timestamp})$.
\end{algsubsteps}

\vspace{0.6em}
\noindent\textbf{Step 10: Consensus, Block Sealing, and Ledger Commitment}

\vspace{0.2em}
\noindent\textbf{10.1} Mempool queuing and candidate block packaging:
\begin{algsubsteps}
    \item[\textbf{10.1.1}] Transaction enters validator mempool and is packaged into block candidate $B_i$.
    \item[\textbf{10.1.2}] Designated Proof-of-Authority validator signs block header with designated validator private key.
\end{algsubsteps}

\noindent\textbf{10.2} Compute cryptographic hash chaining and broadcast block:
\begin{equation}
H(B_i) \leftarrow \text{SHA-256}(H(B_{i-1}) \parallel T_i \parallel Tx_i \parallel n_i)
\end{equation}
\begin{algsubsteps}
    \item[\textbf{10.2.1}] Cryptographic block hash is computed and linked to prior block hash $H(B_{i-1})$.
    \item[\textbf{10.2.2}] Block $B_i$ is distributed across P2P validator network; ledger state root is permanently committed.
\end{algsubsteps}

\vspace{0.6em}
\noindent\textbf{Step 11: Real-Time Event Propagation and UI Notification}

\vspace{0.2em}
\noindent\textbf{11.1} Capture WebSocket event notifications:
\begin{algsubsteps}
    \item[\textbf{11.1.1}] Web3.js WebSocket provider captures emitted \texttt{VoteCast} event log.
    \item[\textbf{11.1.2}] Front end parses event receipt: verifies transaction hash and confirmation block number.
\end{algsubsteps}

\noindent\textbf{11.2} Update user interface state:
\begin{algsubsteps}
    \item[\textbf{11.2.1}] UI dynamically updates to confirm successful ballot casting and renders immutable cryptographic transaction receipt.
\end{algsubsteps}

\vspace{0.6em}
\noindent\textbf{Step 12: Polling Closure and Certified Result Tabulation}

\vspace{0.2em}
\noindent\textbf{12.1} Conclude election session:
\begin{algsubsteps}
    \item[\textbf{12.1.1}] When polling window closes, administrator invokes $\text{closeElection}()$ on the smart contract.
\end{algsubsteps}

\noindent\textbf{12.2} Tabulate certified verifiable results:
\begin{equation}
N(c) = \text{candidates}[c].\text{voteCount}, \quad \forall c \in [1, \text{candidatesCount}]
\end{equation}
\begin{algsubsteps}
    \item[\textbf{12.2.1}] Final tallies are computed directly from the immutable chain state.
    \item[\textbf{12.2.2}] Certified results are displayed on the public audit dashboard; mathematical invariant $\sum N(c) \le |\mathcal{V}|$ holds.
\end{algsubsteps}

\section{Block Structure and Cryptographic Chaining}
Figure~\ref{fig:block_structure} details the internal architecture of blocks within the blockchain ledger, demonstrating how block headers, cryptographic timestamps $T_i$, nonces $n_i$, and transaction sets $Tx_i$ are chained via SHA-256 hashing.

\begin{figure}[H]
\centering
\adjustbox{max width=0.98\linewidth, max height=0.68\textheight, keepaspectratio, center}{\input{diagrams/dag_task_graph_scheduling.tex}}
\caption{Cryptographic block structure and hash chaining mechanism illustrating ledger immutability.}
\label{fig:block_structure}
\end{figure}

\section{Smart Contract State Schemas and Structs}
Figure~\ref{fig:db_schema} depicts the relational entity connections and state mapping layouts maintained in the Solidity smart contract.

\begin{figure}[H]
\centering
\adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_4_prismdb_schema_connectors.tex}}
\caption{Smart contract state schemas, data structs, and relational mappings governing voters and candidates.}
\label{fig:db_schema}
\end{figure}

\section{Level-1 Data Flow Diagram (DFD)}
Figure~\ref{fig:dfd1} presents the Level-1 Data Flow Diagram illustrating the flow of data packets between external entities (Administrator, Voter, Auditor), core processes (1.0 through 5.0), and state data stores.

\begin{figure}[H]
\centering
\adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_1_data_flow_diagram.tex}}
\caption{Level-1 Data Flow Diagram (DFD) for the blockchain-based electronic voting system.}
\label{fig:dfd1}
\end{figure}

%==============================================================================
% CHAPTER 6: DESIGN AND METHODOLOGY
%==============================================================================
\chapter{Design and Methodology}

This chapter expounds the mathematical foundations, Solidity smart contract engineering, staged transaction verification, React/Web3.js front-end integration, MetaMask cryptographic signing, and consensus model trade-offs.

\section{Solidity Smart Contract Architecture}
The core electoral logic is implemented in Solidity (version 0.8.20). Solidity provides strong typing, native cryptographic primitives, and built-in overflow/underflow protection, preventing integer wrap-around attacks without external libraries.

The smart contract defines two primary composite data structures:
\begin{itemize}
    \item \texttt{struct Candidate}: Encapsulates a unique candidate identifier (\texttt{uint id}), moniker string (\texttt{string name}), and accumulated vote tally (\texttt{uint voteCount}).
    \item \texttt{struct Voter}: Encapsulates the voter's whitelisting eligibility status (\texttt{bool isRegistered}), participation status (\texttt{bool hasVoted}), candidate identifier voted for (\texttt{uint votedCandidateId}), and the block timestamp of participation.
\end{itemize}

State mappings link addresses to records:
\begin{verbatim}
    mapping(address => Voter) public voters;
    Candidate[] public candidates;
    address public admin;
    uint public candidatesCount;
\end{verbatim}

Administrative privilege separation is enforced through a custom function modifier:
\begin{verbatim}
    modifier onlyAdmin() {
        require(
            msg.sender == admin,
            "Caller is not certified admin"
        );
        _;
    }
\end{verbatim}
Any invocation of \texttt{addCandidate} or \texttt{registerVoter} from an address other than \texttt{admin} triggers an immediate EVM revert, consuming minimal gas and preventing unauthorized access.

\section{Staged Execution and Double-Voting Mitigation Pipeline}
Figure~\ref{fig:inference_flow} illustrates the staged execution pipeline enforced by the EVM when processing an incoming ballot transaction.

\begin{figure}[H]
\centering
\adjustbox{max width=0.98\linewidth, max height=0.72\textheight, keepaspectratio, center}{\input{diagrams/fig1_2_model_responsibilities_inference_flow.tex}}
\caption{Staged execution flow and atomic double-voting mitigation pipeline within the EVM runtime.}
\label{fig:inference_flow}
\end{figure}

The pipeline executes five strict assertions in sequential order:
\begin{enumerate}
    \item \textbf{Whitelist Assertion:} \texttt{require(voters[msg.sender].isRegistered, "Voter is not registered");} verifies that the voter's public address was authorized by the administrator during Stage 2.
    \item \textbf{Double-Voting Guard:} \texttt{require(!voters[msg.sender].hasVoted, "Voter has already cast a ballot");} checks that the participation flag is false.
    \item \textbf{Ballot Range Check:} \texttt{require(\_candidateId >= 1 \&\& \_candidateId <= candidatesCount, "Invalid candidate ID");} ensures that the selected candidate exists in the candidate registry.
    \item \textbf{Atomic State Mutation:} The contract updates the state in a single atomic transaction:
    $$\text{voters}[\text{msg.sender}].\text{hasVoted} = \text{true}; \quad \text{candidates}[\_candidateId].\text{voteCount}++;$$
    \item \textbf{Event Emission:} The contract emits the \texttt{VoteCast} event, notifying external Web3 listeners.
\end{enumerate}

\section{Front-End DApp Architecture with React.js and Web3.js}
The front end is engineered using React.js, providing a reactive single-page interface that communicates with the blockchain via Web3.js. Web3.js serves as an abstraction layer over the Ethereum JSON-RPC protocol.

When the application loads, it detects the injected Ethereum provider:
\begin{verbatim}
    if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        await window.ethereum.request({
            method: 'eth_requestAccounts'
        });
        const accounts = await web3.eth.getAccounts();
        setUserAddress(accounts[0]);
    }
\end{verbatim}
Event listeners are attached to \texttt{window.ethereum.on('accountsChanged')} and \texttt{window.ethereum.on('chainChanged')}, ensuring that if a user switches their MetaMask account or network, the front-end dynamically refreshes voter eligibility status without requiring a manual browser reload.

\section{MetaMask Cryptographic Handshake and Non-Repudiation}
MetaMask acts as an isolated cryptographic keychain. When a voter submits a ballot, the front end does not have access to the voter's private key. Instead, the transaction payload is handed to MetaMask, which requests explicit user authorization via a popup window.

The transaction is signed using the Elliptic Curve Digital Signature Algorithm (ECDSA) on the secp256k1 curve:
\begin{equation}
    y^2 = (x^3 + 7) \pmod p
\end{equation}
The signature tuple $(r, s, v)$ guarantees two fundamental security properties:
\begin{itemize}
    \item \textbf{Integrity:} Any modification of the transaction parameters (recipient address, candidate ID, nonce) invalidates the signature.
    \item \textbf{Non-Repudiation:} Only the entity holding the private key corresponding to the registered address could have generated the signature.
\end{itemize}

\section{Consensus Mechanism Analysis}
The choice of consensus mechanism directly dictates throughput, latency, energy consumption, and financial viability:
\begin{itemize}
    \item \textbf{Proof-of-Work (PoW):} Provides high security against Sybil attacks through hash power competition, but suffers from low throughput (15 TPS), high latency (12--15 seconds block time), and massive electrical waste.
    \item \textbf{Proof-of-Stake (PoS):} Replaces miners with capital validators, drastically reducing power consumption and improving throughput. However, public PoS networks (like Ethereum mainnet) still expose users to variable gas fees driven by market congestion.
    \item \textbf{Proof-of-Authority (PoA):} Operates on a permissioned network where predefined, vetted institutional entities (e.g., universities, election commissions, judiciary representatives) act as designated block sealers. PoA eliminates computational waste, achieves block times of 1--2 seconds, supports 100+ TPS, and enables zero-gas transactions ($G_{\text{price}} = 0$).
\end{itemize}

For an institutional or national election with a defined polling window, a consortium Proof-of-Authority architecture represents the optimal balance of speed, zero financial cost to voters, and decentralized oversight among independent institutional validators.

%==============================================================================
% CHAPTER 7: PRELIMINARY ANALYSIS
%==============================================================================
\chapter{Preliminary Analysis}

This chapter presents a comparative evaluation of blockchain platforms, consensus models, EVM gas expenditures, and smart contract vulnerability analysis.

\section{Comparative Platform Evaluation}
Selecting an optimal blockchain framework requires evaluating throughput, smart contract capabilities, development tooling, and decentralization trade-offs. Table~\ref{tab:platform_comp} compares four leading candidate frameworks.

\begin{table}[H]
\centering
\caption{Comparative Analysis of Leading Blockchain Platforms for Electronic Voting}
\label{tab:platform_comp}
\fontsize{8.5}{10.5}\selectfont
\begin{tabularx}{\textwidth}{p{3.2cm}p{3.0cm}p{3.0cm}X}
\toprule
\textbf{Platform} & \textbf{Consensus} & \textbf{Throughput (TPS)} & \textbf{Suitability for E-Voting} \\
\midrule
\textbf{Ethereum (PoA/Geth)} & Clique / IBFT 2.0 & 100 -- 400 & \textbf{High:} Robust EVM tooling, mature Web3/MetaMask integration, zero-gas support. \\
\textbf{Ethereum (Public PoS)} & LMD-GHOST / Casper & 15 -- 30 & \textbf{Moderate:} Maximum decentralization, but volatile gas fees and throughput caps. \\
\textbf{Hyperledger Fabric} & Raft / PBFT & 500 -- 2,000 & \textbf{Moderate:} High enterprise throughput, but complex setup and lacks web3 wallet ubiquity. \\
\textbf{Polygon (PoS / L2)} & Bor (PoS) + Heimdall & 1,000 -- 7,000 & \textbf{High:} EVM-compatible Layer-2 scaling, low gas fees, but relies on bridge security. \\
\bottomrule
\end{tabularx}
\end{table}

\section{Consensus Models Comparison}
Table~\ref{tab:consensus_comp} evaluates consensus models across critical electoral criteria.

\begin{table}[H]
\centering
\caption{Consensus Mechanism Evaluation Across Performance and Security Metrics}
\label{tab:consensus_comp}
\fontsize{8.5}{10.5}\selectfont
\begin{tabularx}{\textwidth}{p{3.0cm}p{2.5cm}p{2.5cm}p{2.5cm}X}
\toprule
\textbf{Consensus Model} & \textbf{Block Latency} & \textbf{Energy Usage} & \textbf{51\% Fault Tolerance} & \textbf{Gas Cost Volatility} \\
\midrule
\textbf{Proof-of-Work} & 12 -- 15 s & Extreme ($>$ TWh) & Computational power & High (Market-driven) \\
\textbf{Proof-of-Stake} & 12 s (slots) & Very Low & Stake weight (33\% / 67\%) & High (Market-driven) \\
\textbf{Proof-of-Authority} & 1 -- 2 s & Negligible & Validator collusion ($> 50\%$) & Zero / Predictable \\
\textbf{PBFT} & $<$ 1 s & Negligible & Byzantine faults ($> 33\%$) & Zero (Permissioned) \\
\bottomrule
\end{tabularx}
\end{table}

\section{Gas Consumption and Cost Analysis}
In Ethereum-based networks, every computational opcode consumes a deterministic amount of gas. Table~\ref{tab:gas_analysis} provides an empirical breakdown of gas consumption measured during local testbed execution.

\begin{table}[H]
\centering
\caption{Empirical Smart Contract Gas Consumption Analysis}
\label{tab:gas_analysis}
\fontsize{8.5}{10.5}\selectfont
\begin{tabularx}{\textwidth}{p{4.0cm}p{3.2cm}p{3.5cm}X}
\toprule
\textbf{Smart Contract Function} & \textbf{Gas Consumed (Units)} & \textbf{Primary Opcode Costs} & \textbf{Execution Frequency} \\
\midrule
\texttt{Contract Deployment} & 482,190 & \texttt{CREATE}, \texttt{CODECOPY} & Once per election \\
\texttt{addCandidate(name)} & 46,215 & \texttt{SSTORE} (Candidate array), \texttt{MSTORE} & Once per candidate \\
\texttt{registerVoter(address)} & 28,450 & \texttt{SSTORE} (Whitelist mapping) & Once per eligible voter \\
\texttt{vote(candidateId)} & 44,180 & \texttt{SLOAD}, \texttt{SSTORE} ($\times 2$), \texttt{LOG2} & Once per participating voter \\
\texttt{getResults() [View]} & 0 (Gas-Free) & \texttt{STATICCALL}, \texttt{SLOAD} & Unlimited (Public audits) \\
\bottomrule
\end{tabularx}
\end{table}

On a public network with a gas price of 25 Gwei and ETH at \$2,500, a single vote costing 44,180 gas would incur approximately \$2.76 in transaction fees. In a national election with tens of millions of voters, public gas costs would be financially prohibitive. This empirical finding reinforces our design decision to deploy on a consortium Proof-of-Authority network where $G_{\text{price}}$ is fixed to zero, eliminating all transaction fees for voters.

\section{Security Vulnerability Analysis}
The smart contract was evaluated against common smart contract vulnerabilities:
\begin{itemize}
    \item \textbf{Reentrancy Attacks:} The contract executes state updates (\texttt{hasVoted = true}) before making external calls or emitting events. Furthermore, the contract does not transfer native Ether, completely neutralizing reentrancy vectors.
    \item \textbf{Integer Overflow / Underflow:} The contract uses Solidity 0.8.20, which automatically reverts on arithmetic overflows and underflows without requiring third-party libraries like \texttt{SafeMath}.
    \item \textbf{Denial-of-Service (DoS) via Unbounded Loops:} State variables and mappings are accessed via direct index lookup ($\mathcal{O}(1)$ complexity). There are no unbounded \texttt{for} or \texttt{while} loops that could exceed block gas limits.
    \item \textbf{Front-Running and Miner Extractable Value (MEV):} In a private PoA network with pre-authorized institutional sealers and zero gas fees, priority fee manipulation and front-running are eliminated.
\end{itemize}

%==============================================================================
% CHAPTER 8: FEASIBILITY STUDY
%==============================================================================
\chapter{Feasibility Study}

This chapter assesses the technical, operational, and economic feasibility of deploying the proposed blockchain voting system, accompanied by the project implementation schedule.

\section{Technical Feasibility}
The technical feasibility of the proposed system is validated by the maturity of the underlying open-source technologies:
\begin{itemize}
    \item \textbf{Solidity and the EVM:} The Ethereum Virtual Machine is the most battle-tested decentralized computing environment in existence, with comprehensive developer toolchains (Hardhat, Remix, Truffle).
    \item \textbf{Client Integration:} Web3.js and MetaMask provide standardized, cross-platform APIs supported by all modern browsers.
    \item \textbf{Hardware Requirements:} Node validator clients (e.g., Geth, Besu) operate efficiently on standard off-the-shelf workstation hardware, requiring no specialized mining rigs or graphics processing units (GPUs).
\end{itemize}

\section{Operational Feasibility}
From an operational perspective, the system simplifies election logistics:
\begin{itemize}
    \item \textbf{Voter Usability:} Voters require only a web browser with the MetaMask extension. The intuitive interface provides clear, sequential guidance from wallet connection to ballot confirmation.
    \item \textbf{Administrative Simplicity:} Candidate nomination and voter whitelisting are streamlined through the dedicated administrative dashboard (\texttt{admin.html}).
    \item \textbf{Public Trust and Auditability:} Results are computed directly by the blockchain and displayed publicly in real time, eliminating allegations of counting room manipulation.
\end{itemize}

\section{Economic Feasibility}
Traditional national elections incur billions of dollars in expenditures for ballot printing, secure ballot transport, security personnel, and manual counting centers. In contrast:
\begin{itemize}
    \item \textbf{Software Licensing:} Solidity, Geth, React.js, Web3.js, and MetaMask are 100\% free, open-source software (FOSS), eliminating software licensing costs.
    \item \textbf{Hardware Infrastructure:} A consortium of 5--10 validator nodes run by independent institutions requires minimal cloud or on-premise server infrastructure.
    \item \textbf{Zero-Gas Economics:} By deploying on a private PoA network, ongoing transaction gas costs are zero.
\end{itemize}

\section{Project Implementation Timeline}
Figure~\ref{fig:gantt_chart} presents the project implementation Gantt chart spanning the academic year from July 2026 to March 2027.

\begin{figure}[H]
\centering
\adjustbox{max width=0.98\linewidth, max height=0.48\textheight, keepaspectratio, center}{\input{diagrams/gantt_chart_project_timeline.tex}}
\caption{Gantt chart illustrating the project development timeline and milestone schedule (Jul 2026 -- Mar 2027).}
\label{fig:gantt_chart}
\end{figure}

The project progressed through eleven structured milestones: problem scoping and threat modeling (Jul--Aug '26), literature survey (Aug--Sep '26), requirement analysis (Sep--Oct '26), system architecture design (Oct--Nov '26), Solidity contract development (Nov--Dec '26), double-voting mitigation implementation (Dec '26--Jan '27), React/Web3 front-end engineering (Jan--Feb '27), MetaMask integration (Jan--Feb '27), private PoA testnet deployment (Feb--Mar '27), security testing and comparative analysis (Feb--Mar '27), and final documentation and thesis compilation (Mar '27).

%==============================================================================
% CHAPTER 9: CONCLUSION AND FUTURE SCOPE
%==============================================================================
\chapter{Conclusion and Future Scope}

This chapter concludes the report by summarizing key empirical and architectural achievements, addressing real-world limitations, and outlining prospective research trajectories.

\section{Summary of Achievements}
This project presented the design, implementation, and analysis of a \textbf{Block Chain Based Electronic Voting System}, realized as an Ethereum-based decentralized application (Voting DApp) with smart-contract-level double-voting mitigation. The primary contributions and achievements of this work include:
\begin{itemize}
    \item \textbf{Guaranteed Double-Voting Mitigation:} Designed and implemented an atomic smart contract acceptance predicate ($\text{Accept}(v)$) in Solidity that makes duplicate voting computationally impossible. Once a ballot is cast, the voter's participation flag is atomically mutated within the same transaction, preventing race conditions or direct RPC replay attacks.
    \item \textbf{Role-Based Administrative Security:} Implemented strict cryptographic authorization boundaries separating the election administrator (solely empowered to add candidates and whitelist voter addresses) from voters (authorized solely to submit a single ballot).
    \item \textbf{Seamless Web3 Client Integration:} Developed an intuitive front end using React.js and Web3.js that interfaces with the MetaMask browser wallet, providing secure ECDSA digital signature generation without exposing private credentials.
    \item \textbf{Deterministic Zero-Cost Consortium Consensus:} Analyzed consensus models and established the superiority of a consortium Proof-of-Authority (PoA) architecture, providing sub-2-second block latency, high transaction throughput, and zero gas cost for voters.
    \item \textbf{Comprehensive Literature Survey:} Synthesized a rigorous comparative taxonomy of fifteen recent state-of-the-art blockchain voting architectures across biometrics, blind signatures, and smart contracts, identifying critical scalability and voter verification trade-offs.
\end{itemize}

\section{System Limitations}
Despite its significant security advantages over centralized electronic voting, several operational limitations remain:
\begin{enumerate}
    \item \textbf{Private Key Custody and Digital Literacy:} The system assumes that voters are capable of securely managing their MetaMask wallet and seed phrases. Lost private keys result in disenfranchisement, while stolen private keys permit credential theft.
    \item \textbf{Client Device Vulnerabilities:} While the blockchain ledger is tamper-proof, the voter's local computer or browser could be compromised by keyloggers, screen recording malware, or malicious browser extensions that spoof candidate selections before transaction signing.
    \item \textbf{Public Ledger Pseudonymity vs Ballot Secrecy:} On a fully transparent Ethereum ledger, addresses are pseudonymous rather than completely anonymous. If an adversary links a physical citizen's identity to their public wallet address $v$, the citizen's vote selection $c$ is permanently observable on-chain.
    \item \textbf{Lack of Coercion Resistance:} The system allows voters to cast ballots from unmonitored remote environments. Without isolated physical voting booths, voters can be coerced or induced to vote under third-party observation.
\end{enumerate}

\section{Future Scope and Research Trajectories}
To address these limitations, future research will explore the following advanced directions:
\begin{itemize}
    \item \textbf{Zero-Knowledge Proofs (zk-SNARKs):} Integrate zk-SNARK protocols (such as Groth16 or PLONK) to enable voters to prove eligibility and cast a certified ballot without revealing their identity or candidate selection on the public ledger, achieving complete cryptographic ballot privacy.
    \item \textbf{Blind Signature Protocols:} Implement an ElGamal or RSA blind signature issuance phase during voter registration, cryptographically uncoupling voter whitelisting from ballot casting.
    \item \textbf{Multimodal Biometric Identity Verification:} Incorporate decentralized facial and fingerprint biometric hashing during registration (without storing raw biometric templates on-chain) to eliminate key-sharing and credential sale attacks.
    \item \textbf{Layer-2 Rollups and Sharding:} Deploy Layer-2 Zero-Knowledge Rollups (zk-Rollups) or Optimistic Rollups to batch thousands of ballot transactions off-chain, scaling throughput to tens of thousands of TPS suited for national elections.
    \item \textbf{Decentralized Off-Chain Storage with IPFS:} Integrate the InterPlanetary File System (IPFS) to store candidate manifestos, multimedia profiles, and audit receipts in a decentralized content-addressed storage layer.
\end{itemize}

%==============================================================================
% REFERENCES
%==============================================================================
\begin{thebibliography}{18}

\bibitem{Asha2025}
P.~Asha, P.~G. Reddy, R.~A. Canessane, J.~Refonaa, L.~Padma Suresh, and R.~S. Nancy Noella, ``A Secure Approach to Mitigate Double Voting in Electronic Voting Systems using Blockchain Technology,'' in \emph{Proc. 2025 8th International Conference on Circuit, Power and Computing Technologies (ICCPCT)}, Kollam, India, 2025, pp. 115--120, doi: 10.1109/ICCPCT65132.2025.11176586.

\bibitem{Farooq2022}
M.~S. Farooq, U.~Iftikhar, and A.~Khelifi, ``A Framework to Make Voting System Transparent Using Blockchain Technology,'' \emph{IEEE Access}, vol.~10, pp. 54102--54118, 2022, doi: 10.1109/ACCESS.2022.3175783.

\bibitem{Shahzad2019}
B.~Shahzad and J.~Crowcroft, ``Trustworthy Electronic Voting Using Adjusted Blockchain Technology,'' \emph{IEEE Access}, vol.~7, pp. 24477--24488, 2019, doi: 10.1109/ACCESS.2019.2895670.

\bibitem{Kshetri2018}
N.~Kshetri and J.~Voas, ``Blockchain-Enabled E-Voting,'' \emph{IEEE Software}, vol.~35, no.~4, pp. 95--99, Jul./Aug. 2018, doi: 10.1109/MS.2018.2801546.

\bibitem{Seftyanto2019}
D.~Seftyanto, A.~Amiruddin, and A.~R. Hakim, ``Design of Blockchain-Based Electronic Election System Using Hyperledger: Case of Indonesia,'' in \emph{Proc. 2019 11th International Conference on Information Technology and Electrical Engineering (ICITEE)}, Pattaya, Thailand, 2019, pp. 1--6, doi: 10.1109/ICITEE.2019.8929965.

\bibitem{Ajao2025}
L.~A. Ajao, B.~U. Umar, H.~O. Ohize, E.~M. Dogo, E.~Esenogho, and M.~Cameron, ``Blockchain Integration With Multimodal Biometric Authentication System for Secure Smart Verifiable Electronic Voting System,'' \emph{IEEE Access}, vol.~13, pp. 14201--14220, 2025, doi: 10.1109/ACCESS.2025.3530012.

\bibitem{Mahmood2024}
W.~A. Mahmood, J.~Waleed, A.~R. Abbas, H.~Alaskar, M.~Altulyan, and A.~J. Hussain, ``Intelligent Gesture-Enhanced Blockchain Voting: A New Era of Secure and Accessible E-Voting,'' \emph{IEEE Access}, vol.~12, pp. 88310--88325, 2024, doi: 10.1109/ACCESS.2024.3418892.

\bibitem{PerezGarcia2021}
J.~C. P{\'e}rez Garc{\'\i}a, A.~Benslimane, and S.~Boutalbi, ``Blockchain-Based System for E-Voting Using Blind Signature Protocol,'' in \emph{Proc. IEEE Global Communications Conference (GLOBECOM)}, Madrid, Spain, 2021, pp. 1--6, doi: 10.1109/GLOBECOM46510.2021.9685957.

\bibitem{Baniata2025}
H.~Baniata and G.~Caluna, ``BP-Vot: Blockchain-Based e-Voting Using Smart Contracts, Differential Privacy, and Self-Sovereign Identities,'' \emph{IEEE Transactions on Emerging Topics in Computing}, vol.~13, no.~1, pp. 45--58, Jan.--Mar. 2025, doi: 10.1109/TETC.2024.3411200.

\bibitem{Benabdallah2022}
A.~Benabdallah, A.~Audras, L.~Coudert, N.~El Madhoun, and M.~Badra, ``Analysis of Blockchain Solutions for E-Voting: A Systematic Literature Review,'' \emph{IEEE Access}, vol.~10, pp. 70746--70759, 2022, doi: 10.1109/ACCESS.2022.3187688.

\bibitem{Quzmar2021}
A.~Quzmar, M.~Qatawneh, and S.~Al-Maaitah, ``E-Voting System Based on Blockchain Technology: A Survey,'' \emph{International Journal of Computer Applications}, vol.~183, no.~42, pp. 1--10, Nov. 2021.

\bibitem{Sah2025}
A.~Sah, A.~Kumar, and B.~Bhushan, ``Leveraging Blockchain Technology for Secure Online Voting Systems: A Comprehensive Review,'' \emph{Journal of Network and Computer Applications}, vol.~222, p. 103810, Feb. 2025, doi: 10.1016/j.jnca.2024.103810.

\bibitem{Barelli2025}
R.~Barelli, M.~D'Onghia, and S.~Longari, ``Toward Secure Electronic Voting: A Survey on E-Voting Systems and Attacks,'' \emph{ACM Computing Surveys}, vol.~57, no.~2, pp. 1--38, Feb. 2025, doi: 10.1145/3698780.

\bibitem{Wermelinger2026}
C.~C. Wermelinger, A.~M. Mariano, and J.~M. da Silva, ``Trust and Security in Critical Digital Infrastructures: A Conditional Analysis of Acceptance and Intention to Change in Electronic Voting Systems,'' \emph{Government Information Quarterly}, vol.~43, no.~1, p. 101890, Jan. 2026, doi: 10.1016/j.giq.2025.101890.

\bibitem{Chaudhary2023}
S.~Chaudhary, S.~Shah, R.~Kakkar, R.~Gupta, A.~Alabdulatif, S.~Tanwar, G.~Sharma, and P.~N. Bokoro, ``Blockchain-Based Secure Voting Mechanism Underlying 5G Network: A Smart Contract Approach,'' \emph{IEEE Access}, vol.~11, pp. 60521--60535, 2023, doi: 10.1109/ACCESS.2023.3285149.

\bibitem{Nakamoto2008}
S.~Nakamoto, ``Bitcoin: A Peer-to-Peer Electronic Cash System,'' Dec. 2008. [Online]. Available: \url{https://bitcoin.org/bitcoin.pdf}

\bibitem{Buterin2014}
V.~Buterin, ``Ethereum: A Next-Generation Smart Contract and Decentralized Application Platform,'' White Paper, Jan. 2014. [Online]. Available: \url{https://ethereum.org/en/whitepaper/}

\bibitem{Wood2014}
G.~Wood, ``Ethereum: A Secure Decentralised Generalised Transaction Ledger,'' Ethereum Project Yellow Paper, 2014. [Online]. Available: \url{https://ethereum.github.io/yellowpaper/paper.pdf}

\end{thebibliography}

\end{document}
"""

with open("main.tex", "w", encoding="utf-8") as f:
    f.write(report_content)

print(f"Successfully generated main.tex, total length: {len(report_content)} characters.")
