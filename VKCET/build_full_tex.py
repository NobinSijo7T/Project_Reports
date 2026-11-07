import os
import subprocess
import fitz

def generate_tex_content():
    return r'''\documentclass[12pt,letterpaper]{article}
\usepackage{fontspec}
\setmainfont{Times New Roman}
\usepackage{microtype}

\usepackage[letterpaper, left=99.1pt, right=80.4pt, top=50pt, bottom=40pt, footskip=22pt]{geometry}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{fancyhdr}
\usepackage{tabularx}
\usepackage{array}
\usepackage{colortbl}
\usepackage{xcolor}
\usepackage{enumitem}

\definecolor{tableheader}{gray}{0.95}

\setlength{\parindent}{0pt}
\setlength{\parskip}{7pt}

% Header and Footer configuration
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\fontsize{10.4pt}{12pt}\selectfont\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Custom heading commands
\newcommand{\chaptertitle}[2]{%
  \begin{center}
    {\fontsize{15pt}{18pt}\selectfont\bfseries #1\par}%
    \vspace{2pt}%
    {\fontsize{15pt}{18pt}\selectfont\bfseries #2\par}%
  \end{center}%
  \vspace{10pt}%
}

\newcommand{\singlechaptertitle}[1]{%
  \begin{center}
    {\fontsize{15pt}{18pt}\selectfont\bfseries #1\par}%
  \end{center}%
  \vspace{10pt}%
}

\newcommand{\frontmattertitle}[1]{%
  \begin{center}
    {\fontsize{13.2pt}{16pt}\selectfont\bfseries #1\par}%
  \end{center}%
  \vspace{10pt}%
}

\newcommand{\sectiontitle}[1]{%
  \vspace{6pt}%
  {\noindent\fontsize{13.2pt}{16pt}\selectfont\bfseries #1\par}%
  \vspace{2pt}%
}

\newcommand{\steptitle}[1]{%
  \vspace{4pt}%
  {\noindent\fontsize{11.3pt}{14pt}\selectfont\bfseries #1\par}%
  \vspace{1pt}%
}

\newcommand{\tablecaption}[1]{%
  \begin{center}
    {\fontsize{10.4pt}{12pt}\selectfont #1\par}%
  \end{center}%
  \vspace{2pt}%
}

\newcommand{\bodytextstyle}{\fontsize{11.3pt}{25.8pt}\selectfont}

\begin{document}

% ==================== PAGE 1: TITLE PAGE ====================
\thispagestyle{empty}
\begin{center}
  \vspace*{-16pt}
  {\fontsize{15pt}{17.5pt}\selectfont\bfseries DESIGN OF MULTI-AGENT AUTONOMOUS WORKFLOW\par}
  \vspace{2pt}
  {\fontsize{15pt}{17.5pt}\selectfont\bfseries SYSTEMS USING AGENTIC AI FRAMEWORKS\par}
  \vspace{14pt}
  {\fontsize{11.3pt}{14pt}\selectfont SEMINAR REPORT\par}
  \vspace{10pt}
  {\fontsize{11.3pt}{14pt}\selectfont Submitted by\par}
  \vspace{10pt}
  {\fontsize{13.2pt}{16pt}\selectfont\bfseries SOHAN ANTONTY\par}
  \vspace{2pt}
  {\fontsize{11.3pt}{14pt}\selectfont\bfseries VKE23CS045\par}
  \vspace{16pt}
  {\fontsize{13.2pt}{16pt}\selectfont\bfseries to\par}
  \vspace{8pt}
  {\fontsize{11.3pt}{14pt}\selectfont the APJ Abdul Kalam Technological University, Kerala\par}
  \vspace{6pt}
  {\fontsize{11.3pt}{14pt}\selectfont in partial fulfilment of the requirements for the award of the Degree\par}
  \vspace{6pt}
  {\fontsize{11.3pt}{14pt}\selectfont of\par}
  \vspace{14pt}
  {\fontsize{11.3pt}{14pt}\selectfont Bachelor of Technology\par}
  \vspace{6pt}
  {\fontsize{11.3pt}{14pt}\selectfont In\par}
  \vspace{6pt}
  {\fontsize{11.3pt}{14pt}\selectfont Computer Science and Engineering\par}
  \vspace{14pt}
  \includegraphics[width=135.7pt,height=118.7pt]{figures/page_1_img_29.jpeg}\par
  \vspace{14pt}
  {\fontsize{13.2pt}{16pt}\selectfont\bfseries Department of Computer Science and Engineering\par}
  \vspace{14pt}
  {\fontsize{13.2pt}{16pt}\selectfont Valia Koonambaikulathamma College of Engineering \& Technology\par}
  \vspace{2pt}
  {\fontsize{13.2pt}{16pt}\selectfont Paripally, Thiruvananthapuram\par}
  \vspace{20pt}
  {\fontsize{13.2pt}{16pt}\selectfont SEPTEMBER 2026\par}
\end{center}
\newpage

% ==================== PAGE 2: DECLARATION ====================
\thispagestyle{empty}
\frontmattertitle{DECLARATION}
\vspace{20pt}

\bodytextstyle
I, \textbf{SOHAN ANTONY} hereby declare that the seminar report entitled ``\textbf{Design of Multi-Agent Autonomous Workflow Systems using Agentic AI Frameworks}'' submitted for the partial fulfilment of the requirements for the award of the Degree of Bachelor of Technology in Computer Science and Engineering of APJ Abdul Kalam Technological University, Kerala is a bona fide work carried out under the supervision of RINTU JOHNSON, Assistant professor, Department Of Computer Science and Engineering, Valia Koonambaikulathamma College of Engineering and Technology, Chavarcode, Paripally, Thiruvananthapuram.

I further declare that the material presented in this report is based on the supplied seminar reference material and that the sources used have been acknowledged. I have not knowingly fabricated experimental results or sources. The numerical performance values included in the Results and Discussion chapter are explicitly presented as reported values from the supplied reference paper.

\vspace{40pt}
\noindent
Chavarcode \hfill SOHAN ANTONY\par
\noindent
SEPTEMBER \ 2026
\newpage

% ==================== PAGE 3: CERTIFICATE ====================
\thispagestyle{empty}
\newgeometry{left=72pt, right=72pt, top=50pt, bottom=40pt}
\begin{tikzpicture}[remember picture,overlay]
  \node[anchor=center] at (current page.center) {\includegraphics[width=346.3pt,height=450.7pt]{figures/page_3_img_53.png}};
\end{tikzpicture}

\begin{center}
  \vspace*{16pt}
  {\fontsize{14pt}{17pt}\selectfont\bfseries VALIA KOONAMBAIKULATHAMMA COLLEGE OF\par}
  \vspace{2pt}
  {\fontsize{14pt}{17pt}\selectfont\bfseries ENGINEERING \& TECHNOLOGY\par}
  \vspace{18pt}
  {\fontsize{12pt}{15pt}\selectfont\bfseries DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING\par}
  \vspace{22pt}
  {\fontsize{12pt}{15pt}\selectfont\bfseries CERTIFICATE\par}
\end{center}
\vspace{12pt}

\fontsize{12pt}{27.5pt}\selectfont
\noindent This is to certify that the seminar report entitled ``\textbf{Design of Multi-Agent Autonomous Workflow Systems using Agentic AI Frameworks}'' submitted by \textbf{SOHAN ANTONY [VKE23CS045]}, of the 2023–2027 batch, in partial fulfilment of the requirements for the award of the Degree of Bachelor of Technology in Computer Science and Engineering, APJ Abdul Kalam Technological University, Kerala, is a bonafide record of the seminar work carried out under the guidance.

\vspace{10pt}
\noindent The report has been prepared according to the prescribed academic format and has been reviewed for seminar evaluation.

\vspace{54pt}
\noindent
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}lll@{}}
\textbf{Seminar Guide} & \textbf{Seminar Coordinator} & \textbf{Head of the Department} \\[6pt]
Ms. Rintu Johnson & Ms. Reeba B & Dr. Shine Raj G \\
Assistant Professor & Assistant Professor & Professor \\
Department of CSE & Department of CSE & Department of CSE \\
VKCET & VKCET & VKCET \\
\end{tabular*}
\restoregeometry
\newpage

% ==================== PAGE 4: ACKNOWLEDGEMENT ====================
\pagenumbering{roman}
\setcounter{page}{1}
\frontmattertitle{ACKNOWLEDGEMENT}
\vspace{6pt}

\bodytextstyle
On the submission of this report, I am greatly indebted to all those who helped to complete the seminar on ``Design of Multi-Agent Autonomous Workflow Systems using Agentic AI Frameworks'' and being the part of my seminar.

I would like to express my sincere gratitude and I am deeply in debted to \textbf{Dr. P Sreeraj}, Principal, VKCET, Paripally for his moral support and spirit for the successful completion of this seminar.

I would like to express my sincere thanks to \textbf{Dr Shine Raj G}, Head of the Department, Department of Computer Science and Engineering who has greatly encouraged and supported in doing the seminar by providing all the necessary equipment and facilities.

I would also like to sincerely thank to \textbf{Ms.Reeba B}, Assistant Professor Department of Computer Science and Engineering for coordinating the seminar with such vast dedication and efficiency. Your guidance and support have been crucial in ensuring the success of this event.

I would like to express my immerse gratitude to my guide \textbf{Ms. Rintu Johnson}, Assistant Professor Department of Computer Science and Engineering for her exhilarating supervision and constant encouragement throughout the duration of the seminar.

Finally, let me express my sincere thanks to all staff members of the Department of Computer Science and Engineering and the management of VKCET for supporting and providing all necessary facilities throughout the seminar.

\vspace{12pt}
\hfill {\bfseries SOHAN ANTONY}
\newpage

% ==================== PAGE 5: ABSTRACT ====================
\frontmattertitle{ABSTRACT}
\vspace{6pt}

\bodytextstyle
Artificial Intelligence (AI) is increasingly being used to perform tasks that traditionally require continuous human involvement. A single AI agent can perform a particular task, but complex workflows may contain several related tasks that need to be completed in sequence or in parallel. A Multi-Agent System (MAS) addresses this requirement by using multiple autonomous agents with different roles that communicate and cooperate toward a common goal. This seminar studies the design of Multi-Agent Autonomous Workflow Systems (MAWS) using Agentic AI frameworks. The central idea is to divide a large workflow into smaller tasks, select suitable agents, assign the tasks according to agent capability and availability, allow agents to execute their work, exchange information, and dynamically reassign tasks when workload or environmental conditions change. The reference paper discusses system architecture, agent modelling, the operating environment, dynamic task allocation, communication, learning mechanisms, adaptability, cooperation, autonomy, testing, and continuous improvement. It also discusses the relevance of reinforcement learning, deep learning, and collaborative multi-agent learning in improving autonomous decision-making.

The reported evaluation in the reference material considers task completion time, resource utilization, collaboration efficiency, adaptability, scalability, recovery, and reliability. In the reported agent-count test, completion time decreased from 7.3 hours with 5 agents to 4.2 hours with 20 agents, while reported efficiency increased from 80\% to 90\%. Scenario-based results also report different completion times and resource utilization for healthcare, manufacturing, logistics, and dynamic task-assignment workflows. The paper describes failure recovery and reliability measurements as well. These values are reported results from the supplied reference material and are not newly generated experiments in this seminar.
\newpage

% ==================== PAGE 6: CONTENTS (PART 1) ====================
\thispagestyle{empty}
\vspace*{-10pt}
{\centering\fontsize{13.2pt}{15pt}\selectfont\bfseries CONTENTS\par}
\vspace{8pt}

\begingroup
\setlength{\parskip}{0pt}
\fontsize{11.3pt}{12.4pt}\selectfont
\noindent\textbf{Topics} \hfill \textbf{Page no}\par
\vspace{2pt}
\noindent ACKNOWLEDGEMENT \hfill i\par
\noindent ABSTRACT \hfill ii\par
\noindent LIST OF TABLES \hfill v\par
\noindent ABBREVIATIONS \hfill vi\par
\noindent Chapter 1. INTRODUCTION \hfill 1\par
\noindent\hspace*{28pt} 1.1 General Background \hfill 1\par
\noindent\hspace*{28pt} 1.2 Need for Multi-Agent Autonomous Workflows \hfill 1\par
\noindent\hspace*{28pt} 1.3 Basic Terminology \hfill 2\par
\noindent\hspace*{28pt} 1.4 Scope of the Seminar \hfill 2\par
\noindent\hspace*{28pt} 1.5 Objectives \hfill 3\par
\noindent\hspace*{28pt} 1.6 Organization of the Report \hfill 3\par
\noindent Chapter 2. LITERATURE SURVEY \hfill 4\par
\noindent\hspace*{28pt} 2.1 Overview \hfill 4\par
\noindent\hspace*{28pt} 2.2 Multi-Agent Systems \hfill 4\par
\noindent\hspace*{28pt} 2.3 Agent-Based Programming \hfill 4\par
\noindent\hspace*{28pt} 2.4 Dynamic Task Allocation \hfill 5\par
\noindent\hspace*{28pt} 2.5 Agent Cooperation \hfill 5\par
\noindent\hspace*{28pt} 2.6 Agentic AI \hfill 5\par
\noindent\hspace*{28pt} 2.7 Learning Approaches \hfill 5\par
\noindent\hspace*{28pt} 2.8 Hierarchical Task Networks \hfill 6\par
\noindent\hspace*{28pt} 2.9 Coordination and Mechanism Design \hfill 6\par
\noindent\hspace*{28pt} 2.10 Research Gap and Motivation \hfill 6\par
\noindent\hspace*{28pt} 2.11 Literature Survey Summary Table \hfill 7\par
\noindent Chapter 3. SYSTEM ARCHITECTURE AND METHODOLOGY \hfill 8\par
\noindent\hspace*{28pt} 3.1 System Overview \hfill 8\par
\noindent\hspace*{28pt} 3.2 Agents \hfill 8\par
\noindent\hspace*{28pt} 3.3 Environment \hfill 8\par
\noindent\hspace*{28pt} 3.4 Agentic AI Framework \hfill 8\par
\noindent\hspace*{28pt} 3.5 Task Decomposition \hfill 9\par
\noindent\hspace*{28pt} 3.6 Agent Selection and Dynamic Task Allocation \hfill 9\par
\noindent\hspace*{28pt} 3.7 Communication Layer \hfill 9\par
\noindent\hspace*{28pt} 3.8 Learning Mechanisms \hfill 10\par
\noindent\hspace*{28pt} 3.9 Adaptability \hfill 10\par
\noindent\hspace*{28pt} 3.10 Cooperation \hfill 10\par
\noindent\hspace*{28pt} 3.11 Degree of Autonomy \hfill 10\par
\noindent\hspace*{28pt} 3.12 Testing and Validation \hfill 11\par
\noindent\hspace*{28pt} 3.13 Continuous Improvement \hfill 11\par
\noindent Chapter 4. WORKFLOW AND IMPLEMENTATION \hfill 12\par
\noindent\hspace*{28pt} 4.1 Overall Workflow \hfill 12\par
\noindent\hspace*{56pt} Step 1 – Receive the Task \hfill 12\par
\noindent\hspace*{56pt} Step 2 – Divide the Task \hfill 12\par
\noindent\hspace*{56pt} Step 3 – Select Agents \hfill 12\par
\noindent\hspace*{56pt} Step 4 – Execute Tasks \hfill 12\par
\noindent\hspace*{56pt} Step 5 – Communicate \hfill 13\par
\noindent\hspace*{56pt} Step 6 – Reassign When Needed \hfill 13\par
\noindent\hspace*{56pt} Step 7 – Produce the Final Result \hfill 13\par
\noindent\hspace*{28pt} 4.2 Working Example \hfill 13\par
\noindent\hspace*{28pt} 4.3 Implementation Considerations \hfill 13\par
\noindent\hspace*{28pt} 4.4 Security and Human Oversight Considerations \hfill 14\par
\endgroup
\newpage

% ==================== PAGE 7: CONTENTS (PART 2) ====================
\thispagestyle{empty}
\vspace*{-12pt}
\begingroup
\setlength{\parskip}{0pt}
\fontsize{11.3pt}{12.4pt}\selectfont
\noindent Chapter 5. PERFORMANCE EVALUATION \hfill 15\par
\noindent\hspace*{28pt} 5.1 Evaluation Objectives \hfill 15\par
\noindent\hspace*{28pt} 5.2 Agent-Count Evaluation \hfill 15\par
\noindent\hspace*{28pt} 5.3 Completion Time \hfill 15\par
\noindent\hspace*{28pt} 5.4 System Efficiency \hfill 16\par
\noindent\hspace*{28pt} 5.5 Scenario-Based Evaluation \hfill 16\par
\noindent\hspace*{28pt} 5.6 Collaboration and Adaptability \hfill 16\par
\noindent\hspace*{28pt} 5.7 Reliability and Recovery \hfill 17\par
\noindent\hspace*{28pt} 5.8 Evaluation Limitations \hfill 17\par
\noindent Chapter 6. RESULTS, DISCUSSION, ADVANTAGES AND \hfill \par
\noindent APPLICATIONS \hfill 18\par
\noindent\hspace*{28pt} 6.1 Results Summary \hfill 18\par
\noindent\hspace*{28pt} 6.2 Discussion \hfill 18\par
\noindent\hspace*{28pt} 6.3 Advantages \hfill 18\par
\noindent\hspace*{28pt} 6.4 Healthcare Applications \hfill 19\par
\noindent\hspace*{28pt} 6.5 Manufacturing Applications \hfill 19\par
\noindent\hspace*{28pt} 6.6 Logistics Applications \hfill 19\par
\noindent\hspace*{28pt} 6.7 Autonomous Vehicles \hfill 19\par
\noindent\hspace*{28pt} 6.8 Smart Environments \hfill 20\par
\noindent\hspace*{28pt} 6.9 Limitations \hfill 20\par
\noindent Chapter 7. FUTURE SCOPE \hfill 21\par
\noindent\hspace*{28pt} 7.1 Improved Agent Communication \hfill 21\par
\noindent\hspace*{28pt} 7.2 Intelligent Decision-Making \hfill 21\par
\noindent\hspace*{28pt} 7.3 Larger-Scale Agent Coordination \hfill 21\par
\noindent\hspace*{28pt} 7.4 Improved Learning \hfill 21\par
\noindent\hspace*{28pt} 7.5 Smart Cities \hfill 21\par
\noindent\hspace*{28pt} 7.6 Autonomous Vehicles \hfill 22\par
\noindent\hspace*{28pt} 7.7 Wider Industrial Use \hfill 22\par
\noindent\hspace*{28pt} 7.8 Human-AI Collaboration \hfill 22\par
\noindent CONCLUSION \hfill 23\par
\noindent REFERENCE \hfill 24\par
\endgroup
\newpage

% ==================== PAGE 8: LIST OF TABLES ====================
\setcounter{page}{5}
\frontmattertitle{LIST OF TABLES}
\vspace{16pt}

\fontsize{11.3pt}{16pt}\selectfont
\noindent\begin{tabular*}{\linewidth}{@{}ll@{\extracolsep{\fill}}r@{}}
\textbf{No.} & \textbf{Title} & \textbf{Page No.} \\[10pt]
Table 2.1 & Literature survey summary & 7 \\[8pt]
Table 5.1 & Reported completion time and efficiency for different agent counts & 15 \\[8pt]
Table 5.2 & Reported task completion time and resource utilization across scenarios & 16 \\[8pt]
Table 5.3 & Reported collaboration efficiency and adaptability & 17 \\[8pt]
Table 5.4 & Reported recovery time and system reliability & 17 \\
\end{tabular*}
\newpage

% ==================== PAGE 9: ABBREVIATIONS ====================
\frontmattertitle{ABBREVIATIONS}
\vspace{16pt}

\fontsize{11.3pt}{18.8pt}\selectfont
\noindent\begin{tabular}{@{}p{3.8cm}p{11.2cm}@{}}
\textbf{Abbreviation} & \textbf{Expansion} \\[4pt]
AI & Artificial Intelligence \\
A2A & Agent2Agent \\
AAI & Agentic AI \\
API & Application Programming Interface \\
BDI & Belief–Desire–Intention \\
CMAL & Collaborative Multi-Agent Learning \\
DRL & Deep Reinforcement Learning \\
HTN & Hierarchical Task Network \\
LLM & Large Language Model \\
MAS & Multi-Agent System \\
MAWS & Multi-Agent Autonomous Workflow System \\
ML & Machine Learning \\
NLP & Natural Language Processing \\
RL & Reinforcement Learning \\
SLA & Service-Level Agreement \\
V2X & Vehicle-to-Everything \\
\end{tabular}
\newpage

% ==================== PAGE 10: CHAPTER 1 (REPORT PAGE 1) ====================
\pagenumbering{arabic}
\setcounter{page}{1}
\bodytextstyle

\chaptertitle{CHAPTER 1}{INTRODUCTION}

\sectiontitle{1.1 General Background}
Artificial Intelligence has developed from systems that mainly execute predefined instructions toward systems that can reason about tasks and act with greater autonomy. An AI agent can be understood as an AI system designed to perform a particular task. When several agents with different roles operate together and exchange information, the result is a Multi-Agent System (MAS).

Complex real-world workflows often contain many related activities. Some tasks may be independent and can be performed in parallel, while others depend on information produced by earlier tasks. Traditional workflow systems frequently rely on fixed sequences, manual task assignment, or centralized control. Such arrangements can become difficult to manage when the work load changes, resources become unavailable, or new tasks arrive.

Multi-Agent Autonomous Workflow Systems address this problem by treating the workflow as a team activity. Instead of requiring one system or one person to manage every step, the overall task can be divided into smaller subtasks. Specialized agents can then perform different subtasks, communicate useful information, and adjust task assignments when conditions change. The supplied reference paper presents this approach as a way to improve flexibility, scalability and decision-making in changing environments.

\sectiontitle{1.2 Need for Multi-Agent Autonomous Workflows}
A complex work flow may require different types of expert is eat the same time. For example, a large business workflow may include information gathering, analysis, planning, resource allocation and reporting. Giving every task to a single agent can make the system less flexible and may create a bottleneck. A multi-agent approach distributes responsibilities across agents.
\newpage

% ==================== PAGE 11: (REPORT PAGE 2) ====================
The need for autonomous workflows becomes stronger when the environment is dynamic. New tasks may arrive, priorities may change, or an agent may become unavailable. A fixed workflow may not respond quickly to these changes. Dynamic task allocation allows work to be moved to another suitable agent. Communication allows agents to share status and information. Cooperation allows them to work toward a common objective.

The reference paper therefore focuses on a combination of multi-agent systems and Agentic AI frameworks rather than treating agents as isolated programs.

\sectiontitle{1.3 Basic Terminology}
An AI Agent is an AI-based entity that performs a specific task. A Multi-Agent System is a collection of multiple agents that work in the same problem environment. Agentic AI refers to an approach in which AI systems can perform tasks with greater autonomy, make decisions and coordinate actions.

A workflow is an ordered set of tasks required to achieve an overall goal. Task decomposition means breaking a large task into smaller subtasks. Task allocation means assigning those subtasks to suitable agents. Dynamic task allocation means changing those assignments when the situation changes. Communication is the exchange of information between agents, while cooperation means working together to achieve a shared objective.

\sectiontitle{1.4 Scope of the Seminar}
The seminar concentrates on autonomous workflows formed by multiple cooperating AI agents. It focuses on agent roles, task decomposition, task assignment, autonomous execution, communication, cooperation, dynamic reassignment and performance evaluation.

The seminar does not claim to implement a new production - ready MAWS. The report explains and analyzes the design presented in the supplied 2026 IEEE reference paper and organizes its concepts into a clear workflow-oriented model. Reported numerical results are presented as reference-paper results rather than as experiments conducted for this seminar.
\newpage

% ==================== PAGE 12: (REPORT PAGE 3) ====================
\sectiontitle{1.5 Objectives}
The main objectives identified in the reference material are:
\begin{itemize}[leftmargin=18pt, label=$\bullet$, itemsep=4pt, parsep=0pt, topsep=2pt]
\item Build agentic AI architectures and frameworks that can change and grow.
\item Allow agents to operate independently while cooperating toward common goals.
\item Study how reinforcement learning and col\-lab\-o\-ra\-tive multi-agent learning can improve decision-making.
\item Improve scalability, flexibility and smooth operation as the number of agents increases.
\item Improve real-time task delegation using agent capability, availability, resources and system goals.
\item Examine practical use in healthcare, manufacturing and logistics.
\item Study the effect of Agentic AI frameworks on accuracy, productivity and operational cost.
\end{itemize}

\sectiontitle{1.6 Organization of the Report}
Chapter 1 introduces the topic, motivation, scope and objectives. Chapter 2 reviews relevant research and identifies the research gap. Chapter3 explains the system architecture and methodology. Chapter 4 describes the workflow, steps and implementation considerations. Chapter5 presents the performance measures an reported evaluation. Chapter 6 discusses results, advantages, applications and limitations. Chapter 7 describes future scope, followed by the conclusion, references and appendices.
\newpage

% ==================== PAGE 13: CHAPTER 2 (REPORT PAGE 4) ====================
\chaptertitle{CHAPTER 2}{LITERATURE SURVEY}

\sectiontitle{2.1 Overview}
Research in Multi-Agent Systems has developed across robotics, distributed systems, business process management, healthcare and other domains. Earlier systems often used static task allocation in which tasks were assigned to agents without much ability to modify the workflow. The reference paper identifies this lack of flexibility as a motivation for more adaptive multi-agent models.

The literature discussed in the reference paper covers logic-based multi-agent systems, agent-based programming, dynamic task allocation, cooperation, learning mechanisms, task decomposition, coordination and modern Agentic AI. These areas provide the conceptual foundation for autonomous workflows.

\sectiontitle{2.2 Multi-Agent Systems}
Calegarietal. (2021) is identified as a systematic literature review on logic-based technologies for multi-agent systems. The relevance to this seminar is the broader understanding of how multiple agents can be coordinated as components of a distributed intelligent system.

The key idea carried into MAWS is that agents can have separate responsibilities while still participating in a common coordinated process.

\sectiontitle{2.3 Agent-Based Programming}
Cardoso and Ferrando (2021) review agent-based programming for multi-agent systems. Agent-based approaches provide a conceptual basis for representing autonomous entities, their behavior and interactions.

For MAWS, this supports the idea that agents can be model led as separate entities with roles
\newpage

% ==================== PAGE 14: (REPORT PAGE 5) ====================
and decision-making capabilities, rather than treating the entire workflow as one monolithic program.

\sectiontitle{2.4 Dynamic Task Allocation}
Grosset et al. (2024) is associated in the reference material with dynamic task allocation in autonomous industrial vehicle fleets and V2X cooperation. Dynamic allocation is directly relevant to MAWS because task assignments may need to change according to workload, agent availability and changing requirements. A flexible allocation mechanism prevents a workflow from remaining tied to an unsuitable assignment after the environment changes.

\sectiontitle{2.5 Agent Cooperation}
Mu et al. (2024) surveys cooperation among agents, humans and agents in social dilemmas. Cooperation is important to MAWS because multiple agents may need to exchange information and coordinate their actions to achieve a shared goal.

The reference paper also discusses collaboration as a mechanism for sharing knowledge, resources and planning information.

\sectiontitle{2.6 Agentic AI}
Acharya et al. (2025) provides a recent survey context for Agentic AI and autonomous intelligence for complex goals. The reference paper uses Agentic AI frameworks as a basis for making agents more autonomous, adaptive and capable of decision-making.

The combination of Agentic AI with multi-agent systems is the central theme of this seminar

\sectiontitle{2.7 Learning Approaches}
The reference paper discusses supervised learning, unsupervised learning and reinforcement learning. Supervised learning uses labeled data to learn patterns and predictions. Unsupervised learning identifies patterns without explicit labels. Reinforcement learning allows an agent to
\newpage

% ==================== PAGE 15: (REPORT PAGE 6) ====================
interact with an environment and learn from feedback such as rewards or penalties.

Deep Reinforcement Learning (DRL) and Collaborative Multi-Agent Learning (CMAL) are specifically highlighted as mechanisms that can support autonomous decision-making, cooperation and scalability

\sectiontitle{2.8 Hierarchical Task Networks}
Hierarchical Task Networks (HTNs) are discussed as a method for decomposing complex tasks into simpler subtasks. This is closely related to MAWS because a large workflow can first be represented at a high level and then divided into manageable units that can be assigned to different agents.

The approach is especially relevant to workflows in which several dependent activities must be coordinated.

\sectiontitle{2.9 Coordination and Mechanism Design}
The reference paper discusses game theory, auction theory and mechanism design as approaches that have been used to improve coordination and resolve conflicts among agents. These approaches can help agents make decisions about resources and task allocation when multiple agents compete for or depend on the same resources.

\sectiontitle{2.10 Research Gap and Motivation}
The literature and reference paper indicate several practical gaps. Many workflows still depend on manual control and fixed task assignment. Traditional centralized systems can be less flexible when the workload or environment changes. As the number of tasks and agents grows, coordination and communication become more difficult.

The motivation for MAWS is therefore to combine task decomposition, automatic agent selection, autonomous execution, communication, cooperation and dynamic reassignment in one workflow-oriented architecture. The aim is not simply to add more agents, but to
\newpage

% ==================== PAGE 16: (REPORT PAGE 7) ====================
coordinate them effectively so that the overall system remains useful as the environment changes.

\sectiontitle{2.11 Literature Survey Summary Table}
\tablecaption{Table 2.1 Literature survey summary}

\fontsize{8pt}{10.5pt}\selectfont
\noindent\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash}p{3.2cm}|>{\centering\arraybackslash}p{3.5cm}|>{\arraybackslash}X|}
\hline
\rowcolor{tableheader}
\textbf{Author / Year} & \textbf{Focus} & \textbf{Contribution / Relevance} \\
\hline
Calegari et al. (2021) & Multi-Agent Systems & Systematic review of logic-based technologies for MAS; provides conceptual foundation. \\
\hline
Cardoso \& Ferrando (2021) & Agent-Based Systems & Reviews agent-based programming and autonomous agent interaction. \\
\hline
Grosset et al. (2024) & Dynamic Task Allocation & Addresses dynamic task allocation in autonomous industrial vehicle fleets. \\
\hline
Mu et al. (2024) & Agent Cooperation & Surveys cooperation among agents , humans and agents. \\
\hline
Acharya et al. (2025) & Agentic AI & Provides recent context for autonomous intelligence for complex goals. \\
\hline
\end{tabularx}
\newpage

% ==================== PAGE 17: CHAPTER 3 (REPORT PAGE 8) ====================
\bodytextstyle
\chaptertitle{CHAPTER 3}{SYSTEM ARCHITECTURE AND METHODOLOGY}

\sectiontitle{3.1 System Overview}
A Multi-Agent Autonomous Workflow System contains several connected components: agents, an operating environment, an Agentic AI framework, task allocation mechanisms and a communication layer. Together these components allow the system to receive a workflow, divide it into tasks, assign work, execute subtasks, exchange information and adapt to changes.

\sectiontitle{3.2 Agents}
Agents are the main active components of MAWS. Each agent is responsible for a particular job or group of jobs. An agent can work independently while contributing to the overall workflow. Agents may differ in capabilities, availability and workload. The architecture therefore does not assume that every agent is equally suitable for every task. The system selects agents according to the requirements of the subtask and the current state of the workflow.

\sectiontitle{3.3 Environment}
The environment is the situation in which agents operate. It provides information such as tasks, resource status and operational conditions. The environment may be physical, such as a factory or delivery route, or abstract, such as a scheduling and decision-making environment.

Agent actions can change the state of the environment. For example, completing a task changes the set of remaining tasks and may make new information available to other agents.

\sectiontitle{3.4 Agentic AI Framework}
The Agentic AI framework provides the algorithms and tools that support agent decision-making and task execution. The reference paper discusses machine learning, reinforcement learning and deep learning as possible components.
\newpage

% ==================== PAGE 18: (REPORT PAGE 9) ====================
The framework also supports communication and coordination so that individual agents can participate inthe larger workflow. The important point is that the framework provides the agents with a structured way to observe, decide, act and communicate.

\sectiontitle{3.5 Task Decomposition}
Task decomposition is the first major workflow operation. The overall task is divided into smaller subtasks. Decomposition reduces the complexity of the original task and makes it possible to distribute work.

For example, a large workflow can be divided into information collection, analysis, planning and reporting. The actual subtasks depend on the application and are not fixed by the architecture.

\sectiontitle{3.6 Agent Selection and Dynamic Task Allocation}
After decomposition, suitable agents are selected for the subtasks. The reference paper states that allocation can consider capability, availability and current work load. Dynamic allocation is important because the state of the system can change after the initial assignment.

If an agent becomes unavailable or a task becomes more urgent, the system can redistribute work. This prevents the workflow from remaining locked to an assignment that is no longer suitable.

\sectiontitle{3.7 Communication Layer}
The communication layer allows agents to exchange task updates, data, status and other relevant information. The reference paper discusses both synchronous and asynchronous communication. Synchronous communication is useful when an agent needs an immediate response. Asynchronous communication allows agents to continue working and exchange messages without requiring all participants to act at exactly the same time. A robust communication layer is therefore important for coordination.
\newpage

% ==================== PAGE 19: (REPORT PAGE 10) ====================
\sectiontitle{3.8 Learning Mechanisms}
The reference paper identifies supervised learning, unsupervised learning and reinforcement learning as useful learning mechanisms. Reinforcement learning is particularly important for autonomous decision-making because agents can learn from feedback received after actions.

Deep learning can support complex data processing, while collaborative multi-agent learning can allow agents to learn or improve through interaction with other agents.

\sectiontitle{3.9 Adaptability}
Adaptability means the ability to change actions when the environment changes. Examples include changing workload, new tasks, resource availability or changing deadlines. When conditions change, the system can recalculate task allocation, reassign jobs or choose a different allocation.

The reference paper gives examples such as rerouting delivery tasks in response to changing traffic conditions and real locating healthcare  resources  based on patient urgency.

\sectiontitle{3.10 Cooperation}
Agents can work independently but still cooperate toward a common objective. Cooperation may involve sharing information, sharing resources, coordinating schedules and solving subtasks that are difficult for a single agent.

A successful multi-agent workflow therefore requires both local agent autonomy and system-level coordination.

\sectiontitle{3.11 Degree of Autonomy}
The level of agent independence can be adjusted according to the application. Low autonomy allows agents to perform routine tasks with substantial human oversight. High autonomy allows agents to make decisions without continuous human involvement. Other tasks may require greater supervision or approval.

This flexibility is important because not every application should operate with the same level of
\newpage

% ==================== PAGE 20: (REPORT PAGE 11) ====================
autonomy. The reference paper recognizes that human oversight may still be necessary in complex or sensitive situations.

\sectiontitle{3.12 Testing and Validation}
The methodology proposes testing the system in a simulated environment. Different conditions can be created, such as increased task difficulty or reduced resource availability. Performance can then be evaluated using measures such as task completion time, resource utilization and system efficiency.

The reference paper also describes real-world pilot evaluation and feedback-based improvement. For this seminar, these are discussed as part of the reference paper's methodology rather than as newly conducted experiments.

\sectiontitle{3.13 Continuous Improvement}
After evaluation, the system can be improved using performance feedback. Agents can learn from the results of their actions, and the workflow can be updated for new tasks, environmental conditions or user needs.

Continuous monitoring is also important for scalability because increasing the number of agents can introduce additional communication and coordination requirements.
\newpage

% ==================== PAGE 21: CHAPTER 4 (REPORT PAGE 12) ====================
\chaptertitle{CHAPTER 4}{WORKFLOW AND IMPLEMENTATION}

\sectiontitle{4.1 Overall Workflow}
The workflow can be represented as:

\vspace{2pt}
\noindent Overall Task $\rightarrow$ Task Decomposition $\rightarrow$ Agent Selection and Assignment $\rightarrow$ Agent Execution $\rightarrow$ Communication and Cooperation $\rightarrow$ Dynamic Reassignment $\rightarrow$ Final Result\par
\vspace{4pt}

This sequence represents the core design described in the seminar material.

\steptitle{Step 1 – Receive the Task}
The system first receives an overall task or workflow objective. The task describes what the system is expected to accomplish. At this stage, the system identifies the goal and the information needed to begin processing.

\steptitle{Step 2 – Divide the Task}
The overall task is divided into smaller subtasks. The purpose is to create units of work that can be handled by suitable agents. The decomposition can reflect dependencies between tasks so that tasks requiring earlier results are scheduled accordingly.

\steptitle{Step 3 – Select Agents}
The system identifies agents whose capabilities match the subtasks. Availability and current workload can also be considered. The objective is to avoid assigning a task to an unsuitable or overloaded agent when another suitable agent is available.

\steptitle{Step 4 – Execute Tasks}
Selected agents perform their assigned subtasks. Each agent focuses on its role while maintaining awareness of relevant workflow information. Agents can operate with reduced continuous human control according to the required level of autonomy.
\newpage

% ==================== PAGE 22: (REPORT PAGE 13) ====================
\steptitle{Step 5 – Communicate}
During execution, agents exchange useful information such as progress, task results, status and resource changes. Communication allows one agent's output to become useful input for another agent.

\steptitle{Step 6 – Reassign When Needed}
If the environment changes, the original allocation may no longer be suitable. The system can reassign tasks based on the new state. Examples include a change in priority, increased workload or an unavailable agent.

\steptitle{Step 7 – Produce the Final Result}
After subtasks are completed, the outputs are combined or coordinated to produce the overall workflow result. The final result represents the collective work of the agents rather than the output of only one agent.

\sectiontitle{4.2 Working Example}
Consider a generic logistics workflow. The overall objective is to complete a set of deliveries. One group of agents can handle delivery information, another can handle route-related decisions, and another can monitor resource or vehicle status. If a route becomes unsuitable, the system can reassign work or update the plan. The example illustrates the principle of specialization, communication and dynamic adaptation without depending on a specific software implementation.

\sectiontitle{4.3 Implementation Considerations}
A practical implementation would require an agent manager or orchestration mechanism, agent definitions, a task queue, a communication mechanism, access to workflow data, decision logic and monitoring. The exact software stack is not specified in the supplied reference paper, so this report does not claim a particular framework or programming language as the
\newpage

% ==================== PAGE 23: (REPORT PAGE 14) ====================
implemented system.

The architecture can nevertheless be mapped to software components: a workflow input module, task decomposition module, agent registry, allocation module, communication service, execution modules, monitoring module and result coordinator.

\sectiontitle{4.4 Security and Human Oversight Considerations}
Autonomous systems should be designed with appropriate control because agents may make decisions that affect resources or workflows. The reference material explicitly notes that human supervision may still be required in some situations.

A practical system should therefore support monitoring, logging, controlled permissions and the ability to intervene when a workflow reaches a sensitive or uncertain state. These are implementation considerations rather than new claims from the reference experiments.
\newpage

% ==================== PAGE 24: CHAPTER 5 (REPORT PAGE 15) ====================
\chaptertitle{CHAPTER 5}{PERFORMANCE EVALUATION}

\sectiontitle{5.1 Evaluation Objectives}
The reference paper evaluates MAWS using several performance dimensions: task completion time, resource utilization, collaboration efficiency, adaptability, scalability, recovery time and reliability. These measures help determine whether the system can complete workflows efficiently while responding to changes and failures.

\sectiontitle{5.2 Agent-Count Evaluation}
The supplied seminar material reports the following values for increasing numbers of agents. These are reference-paper results and are reproduced for analysis.

\tablecaption{Table 5.1 Reported completion time and efficiency for different agent counts}
\fontsize{8pt}{10.5pt}\selectfont
\noindent\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash}X|>{\centering\arraybackslash}X|>{\centering\arraybackslash}X|}
\hline
\rowcolor{tableheader}
\textbf{Agents} & \textbf{Completion Time} & \textbf{Efficiency} \\
\hline
5 & 7.3 hours & 80\% \\
\hline
10 & 5.2 hours & 85\% \\
\hline
15 & 4.5 hours & 87\% \\
\hline
20 & 4.2 hours & 90\% \\
\hline
\end{tabularx}
\vspace{2pt}

\bodytextstyle
\sectiontitle{5.3 Completion Time}
The reported task completion time decreases from 7.3 hours with 5 agents to 4.2 hours with 20 agents. The trend suggests that distributing work among more agents can reduce completion time in the presented test.

However, the result should not be interpreted as meaning that adding agents will always improve performance without limit. The same reference material identifies communication and coordination complexity as scalability challenges.
\newpage

% ==================== PAGE 25: (REPORT PAGE 16) ====================
\bodytextstyle
\sectiontitle{5.4 System Efficiency}
Reported efficiency increases from 80\% with 5 agents to 90\% with 20 agents. Within the presented test, this is associated with better workflow performance as work is distributed among more agents.

The supplied material does not provide a precise mathematical definition of the efficiency metric, so this report does not invent one.

\sectiontitle{5.5 Scenario-Based Evaluation}
The reference paper also reports results for healthcare, manufacturing, logistics and dynamic task-assignment scenarios. The healthcare workflow is reported with 8 agents, 3.5 hours average task completion time and 90\% resource utilization. Manufacturing is reported with 10 agents, 5.2 hours and 85\% resource utilization. Logistics is reported with 12 agents, 6.1 hours and 80\% resource utilization. Dynamic task assignment is reported with 15 agents, 4.9 hours and 83\% resource utilization.

\tablecaption{Table 5.2 Reported task completion time and resource utilization across scenarios}
\fontsize{8pt}{10.5pt}\selectfont
\noindent\begin{tabularx}{\linewidth}{|>{\arraybackslash}p{4.2cm}|>{\centering\arraybackslash}p{2.2cm}|>{\centering\arraybackslash}p{3.2cm}|>{\centering\arraybackslash}X|}
\hline
\rowcolor{tableheader}
\textbf{Scenario} & \textbf{Agents} & \textbf{Completion Time} & \textbf{Resource Utilization} \\
\hline
Manufacturing Workflow & 10 & 5.2 h & 85\% \\
\hline
Healthcare Workflow & 8 & 3.5 h & 90\% \\
\hline
Logistics Workflow & 12 & 6.1 h & 80\% \\
\hline
Dynamic Task Assignment & 15 & 4.9 h & 83\% \\
\hline
\end{tabularx}
\vspace{2pt}

\bodytextstyle
\sectiontitle{5.6 Collaboration and Adaptability}
The reference paper reports collaboration efficiency of 92\% for healthcare, 88\% for manufacturing, 85\% for logistics and 90\% for dynamic task assignment. Adaptability time is reported as 5, 7, 6 and 4 minutes respectively.

These results indicate that the reference evaluation considered not only completion time but also how well agents cooperate and how quickly the workflow can respond to changes.
\newpage

% ==================== PAGE 26: (REPORT PAGE 17) ====================
\tablecaption{Table 5.3 Reported collaboration efficiency and adaptability}
\fontsize{8pt}{10.5pt}\selectfont
\noindent\begin{tabularx}{\linewidth}{|>{\arraybackslash}p{5.5cm}|>{\centering\arraybackslash}p{5cm}|>{\centering\arraybackslash}X|}
\hline
\rowcolor{tableheader}
\textbf{Scenario} & \textbf{Collaboration Efficiency} & \textbf{Adaptability} \\
\hline
Healthcare Workflow & 92\% & 5 min \\
\hline
Manufacturing Workflow & 88\% & 7 min \\
\hline
Logistics Workflow & 85\% & 6 min \\
\hline
Dynamic Task Assignment & 90\% & 4 min \\
\hline
\end{tabularx}
\vspace{2pt}

\bodytextstyle
\sectiontitle{5.7 Reliability and Recovery}
The reference paper reports recovery time and reliability for failure scenarios. Agent failure is reported with a recovery time of 2 minutes and system reliability of 98\%. Resource failure is reported with 3 minutes and 97\% reliability, while task overload is reported with 4 minutes and 96\% reliability.

These values indicate that the paper considered the ability of the system to continue operating when a component or resource becomes unavailable.

\tablecaption{Table 5.4 Reported recovery time and system reliability}
\fontsize{8pt}{10.5pt}\selectfont
\noindent\begin{tabularx}{\linewidth}{|>{\arraybackslash}p{5.5cm}|>{\centering\arraybackslash}p{5cm}|>{\centering\arraybackslash}X|}
\hline
\rowcolor{tableheader}
\textbf{Scenario} & \textbf{Recovery Time} & \textbf{Reliability} \\
\hline
Agent Failure & 2 min & 98\% \\
\hline
Resource Failure & 3 min & 97\% \\
\hline
Task Overload & 4 min & 96\% \\
\hline
\end{tabularx}
\vspace{2pt}

\bodytextstyle
\sectiontitle{5.8 Evaluation Limitations}
The supplied reference material does not provide complete details of experimental hardware, datasets, statistical significance testing or a formal mathematical definition of every performance. Therefore, the reported values should be understood as the values presented in the reference paper rather than independently verified experimental results for this seminar.
\newpage

% ==================== PAGE 27: CHAPTER 6 (REPORT PAGE 18) ====================
\bodytextstyle
\chaptertitle{CHAPTER 6}{RESULTS, DISCUSSION, ADVANTAGES AND APPLICATIONS}

\sectiontitle{6.1 Results Summary}
The overall reported results indicate that MAWS can improve workflow handling when multiple agents cooperate. The agent-count test associates an increase from 5 to 20 agents with a reduction in completion time from 7.3 to 4.2 hours and an increase in reported efficiency from 80\% to 90\%.

The scenario-based results also show that the system was evaluated across different workflow characteristics. Healthcare achieved 3.5 hours and 90\% resource utilization, while dynamic task assignment achieved 4.9 hours and 83\% resource utilization. Fault-recovery results report recovery times of 2 to 4 minutes and reliability between 96\% and 98\%.

\sectiontitle{6.2 Discussion}
These results support the conceptual benefits of multi-agent workflows. Dividing work allows tasks to be handled concurrently or by specialized agents. Dynamic task allocation allows the system to respond when tasks or resources change.

At the same time, the results must be viewed within the limits of the reported setup. The reference paper does not show that adding agents will always improve performance indefinitely. Coordination overhead, communication delays and resource contention can limit scalability in larger systems.

\sectiontitle{6.3 Advantages}
The reference material identifies several advantages:
\begin{enumerate}[leftmargin=20pt, label=\arabic*., itemsep=3pt, parsep=0pt, topsep=2pt]
\item Reduced need for continuous manual task handling.
\item Distribution of complex work among multiple agents.
\end{enumerate}
\newpage

% ==================== PAGE 28: (REPORT PAGE 19) ====================
\bodytextstyle
\begin{enumerate}[leftmargin=20pt, label=\arabic*., itemsep=3pt, parsep=0pt, topsep=0pt, start=3]
\item Communication and cooperation between agents.
\item Dynamic adaptation when conditions change.
\item Support for multiple tasks in parallel or coordinated stages.
\item Potential improvement in workflow efficiency.
\item Ability to continue operating through some failures using recovery mechanisms.
\end{enumerate}

\sectiontitle{6.4 Healthcare Applications}
In healthcare environments, workflows may include patient intake, diagnostic test scheduling, medical records management and resource allocation. Autonomous agents can help coordinate these tasks by routing requests, updating schedules and alerting human staff when high-priority situations arise.

\sectiontitle{6.5 Manufacturing Applications}
In manufacturing, agents can monitor assembly lines, track inventory and coordinate machinery. If a machine requires maintenance or a supply delay occurs, the system can dynamically adjust task allocations to reduce idle time and maintain production.

\sectiontitle{6.6 Logistics Applications}
In logistics, workflows involve package sorting, route planning, fleet tracking and delivery updates. Agents can analyze traffic conditions, delivery windows and vehicle availability to adapt delivery schedules dynamically.

\sectiontitle{6.7 Autonomous Vehicles}
The reference paper identifies autonomous driving and changing situations as an application area. Multiple agents can support decision-making and coordination in environments where conditions change in real time.
\newpage

% ==================== PAGE 29: (REPORT PAGE 20) ====================
\bodytextstyle
\sectiontitle{6.8 Smart Environments}
Future-oriented applications includes mart environments and smart cities, where multiple intelligent services may need to coordinate information and resources. The multi-agent approach can provide a framework for managing complex interactions among distributed devices and services.

\sectiontitle{6.9 Limitations}
Although MAWS offers notable benefits, several practical limitations should be recognized:

\steptitle{6.9.1 Managing many agents becomes difficult as system size increases.}
As the number of agents grows, tracking agent status, preventing conflicting decisions and ensuring global consistency become more complex.

\steptitle{6.9.2 Communication becomes more complex when more agents interact.}
Higher agent counts increase message volume and network overhead. Communication delays can reduce responsiveness if protocols are inefficient.

\steptitle{6.9.3 Larger systems require additional computing resources}
Running multiple reasoning agents simultaneously demands substantial computational power, memory and infrastructure support.

\steptitle{6.9.4 Complex workflows need stronger coordination mechanisms.}
Workflows with intricate inter-task dependencies require sophisticated orchestration to avoid deadlocks, race conditions or redundant execution.

These limitations show that autonomy and scalability introduce engineering challenges. A successful MAWS must therefore balance agent independence with system-level control and coordination.
\newpage

% ==================== PAGE 30: CHAPTER 7 (REPORT PAGE 21) ====================
\bodytextstyle
\chaptertitle{CHAPTER 7}{FUTURE SCOPE}

\sectiontitle{7.1 Improved Agent Communication}
Future systems can improve the reliability, speed and efficiency of communication among agents. Better protocols can reduce unnecessary messages, prioritize urgent updates and allow agents to interact smoothly across different platforms and networks.

\sectiontitle{7.2 Intelligent Decision-Making}
Future agents can incorporate more advanced decision algorithms, including improved reinforcement learning and large model integration. These improvements can allow agents to better evaluate uncertainty, anticipate failures and choose effective workflow actions.

\sectiontitle{7.3 Larger-Scale Agent Coordination}
Further work is needed on scaling multi-agent systems to very large numbers of agents. Research can address how to maintain cooperation and avoid communication bottlenecks as the number of agents and tasks expands.

\sectiontitle{7.4 Improved Learning}
Collaborative learning mechanisms can allow agents to learn not only from their own experience but also from the actions and feedback of other agents. This can improve workflow performance across repeated tasks.

\sectiontitle{7.5 Smart Cities}
Smart-city environments contain many services such as transport, resource management and coordinated public services. Multi-agent workflows could allow these services to operate as cooperating intelligent components.
\newpage

% ==================== PAGE 31: (REPORT PAGE 22) ====================
\bodytextstyle
\sectiontitle{7.6 Autonomous Vehicles}
The reference paper identifies self-driving vehicles as a future application. Multi-agent coordination could support decision-making in changing traffic and operational conditions.

\sectiontitle{7.7 Wider Industrial Use}
The approach can be extended to additional industries and smart environments where tasks are interdependent, resources are shared and conditions change over time.

\sectiontitle{7.8 Human-AI Collaboration}
Future systems can combine autonomy with controlled human oversight. Instead of completely removing humans, the system can allow people to supervise important decisions, handle exceptional cases and intervene when the agents are uncertain.
\newpage

% ==================== PAGE 32: CONCLUSION (REPORT PAGE 23) ====================
\bodytextstyle
\singlechaptertitle{CONCLUSION}

Multi-Agent Autonomous Workflow Systems provide a practical approach for handling complex workflows through cooperation among multiple AI agents. Instead of depending on one AI system or continuous manual control, a large workflow can be divided into smaller tasks and assigned to suitable agents. Agents can execute their roles, communicate information and adapt task assignments when conditions change. The reference paper combines multi-agent systems with Agentic AI frameworks to support autonomy, learning, cooperation, dynamic task allocation and adaptability. The methodology includes system design, agent modeling, environment setup, task allocation, communication, testing and continuous improvement. The reported evaluation associates an increase from 5 to 20 agents with a decrease in completion time from 7.3 hours to 4.2 hours and an increase in reported efficiency from 80\% to 90\%. Additional scenario-based results cover healthcare, manufacturing, logistics and dynamic task assignment, while failure tests report recovery and reliability values. These results are treated in this report as reference-paper findings rather than newly generated experiments. The approach has potential in healthcare, manufacturing, logistics, autonomous vehicles and smart environments. However, increasing the number of agents can also increase communication, coordination and computing requirements. Human supervision may remain necessary for complex or sensitive situations. Future work can focus on improved communication, decision-making, learning, scalability, smart-city applications, autonomous vehicles and wider industrial use.
\newpage

% ==================== PAGE 33: REFERENCES (PART 1) ====================
\thispagestyle{empty}
\newgeometry{left=72pt, right=72pt, top=50pt, bottom=40pt}
\begin{center}
  {\fontsize{14pt}{17pt}\selectfont\bfseries REFERENCES\par}
\end{center}
\vspace{10pt}

\begingroup
\sloppy
\fontsize{12pt}{25.8pt}\selectfont
\noindent 1. R.Calegari, G.Ciatto, V.Mascardi, A.Omicini, ``\textit{Logic-based technologies for multi-agent systems: a systematic literature review},'' Autonomous Agents and Multi-Agent Systems, 35(1), 2021.

\vspace{6pt}
\noindent 2. R.C.Cardoso, A.Ferrando, ``\textit{A review of agent-based programming for multi-agent systems},''Computers,10(2), 2021.

\vspace{6pt}
\noindent 3. J. Grosset, A.-J. Fougères, M. Djoko-Kouam, J.-M. Bonnin, ``\textit{Multi-agent simulation of autonomous industrial vehicle fleets: Towards dynamic task allocation in V2X cooperation mode},''Integrated Computer-Aided Engineering, 31(3), pp. 249–266, 2024.

\vspace{6pt}
\noindent 4. C.Mu,H.Guo,Y.Chen,C.Shen,D.Hu,S.Hu,Z.Wang,``\textit{Multi-agent,human–agent and beyond: a survey on cooperation in social dilemmas},'' Neuro computing, 610, Article 128514, 2024.

\vspace{6pt}
\noindent 5. A.Saadi,R.Maamri,Z.Sahnoun, ``\textit{Behavioral flexibility in belief-desire-intention(BDI) architectures},'' Multi agent and Grid Systems, 16(4), pp. 343–377, 2020.

\vspace{6pt}
\noindent 6. D.B.Acharya, K.Kuppan, B.Divya, ``\textit{Agentic AI: Autonomous intelligence for complex goals–a comprehensive survey},'' IEEE Access, 2025.

\vspace{6pt}
\noindent 7. L.Hughes, Y.K.Dwivedi, T.Malik, M.Shawosh, M.A.Albashrawi, I.Jeon, V.Dutot, M.Appanderanda, T.Crick, R.De',etal.,``\textit{AI agents and agentic systems: A multi-expert analysis},'' Journal of Computer Information Systems, pp. 1–29, 2025.

\vspace{6pt}
\noindent 8. M.Gridach, J.Nanavati, K.Z.E.Abidine, L.Mendes, C.Mack, ``\textit{Agentic AI for scientific discovery: A survey of progress, challenges, and future directions},'' 2025.
\endgroup
\newpage

% ==================== PAGE 34: REFERENCES (PART 2) ====================
\thispagestyle{empty}
\begingroup
\sloppy
\fontsize{12pt}{25.8pt}\selectfont
\noindent 9. T. Song, M. Luo, X. Zhang, L. Chen, Y. Huang, J. Cao, Q. Zhu, D. Liu, B. Zhang, G. Zou, et al., ``\textit{A multiagent-driven robotic AI chemist enabling autonomous chemical research on demand},'' Journal of the American Chemical Society, 147(15), pp. 12534–12545, 2025.

\vspace{6pt}
\noindent 10. A.Zhang, Y.Chen, L.Sheng, X.Wang, T.-S.Chua, ``\textit{On generative agents in recommendation},'' Proceedings of the 47th International ACM SIGIR Conference, pp. 1807–1817, 2024.

\vspace{6pt}
\noindent 11. Z.Liu,T.Hoang,J.Zhang,M.Zhu,T.Lan,J.Tan,W.Yao,Z.Liu,Y.Feng,R.RN,etal.,``\textit{Apigen:Automated pipeline for generating verifiable and diverse function-calling datasets},'' Advances in Neural Information Processing Systems, 37, pp. 54463–54482, 2024.

\vspace{6pt}
\noindent 12. I.Hettiarachchi, ``\textit{Exploring generative AI agents: Architecture, applications, and challenges},'' Journal of Artificial Intelligence and General Science, 8(1), pp. 105–127, 2025.

\vspace{6pt}
\noindent 13. R.Surapaneni, J.Miku, M.Vakoc, T.Segal, ``\textit{Announcing the Agent 2 Agent protocol(A2A)},''Google Developers Blog, 2025.

\vspace{6pt}
\noindent 14. Z.Duan,J.Wang, ``\textit{Exploration of LL Mmulti-agent application implementation based on Lang Graph+CrewAI},'' 2024.
\endgroup
\restoregeometry

\end{document}
'''

content = generate_tex_content()

# Write to both main.tex and report.tex
with open("main.tex", "w", encoding="utf-8") as f:
    f.write(content)
with open("report.tex", "w", encoding="utf-8") as f:
    f.write(content)

print("Saved main.tex and report.tex")