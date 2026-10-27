import os

filepath = r"c:\Users\nobin\OneDrive\Documents\Projects\PROJECT_REPORTS\Adeeba\main.tex"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

start_kw = r"\section{Smart Contract State Schemas and Structs}"
end_kw = r"\clearpage"

p1 = text.find(start_kw)
p2 = text.find(end_kw, p1)

if p1 == -1 or p2 == -1:
    print(f"Error finding markers: p1={p1}, p2={p2}")
    exit(1)

content = r"""\section{Smart Contract State Schemas and Structs}
\enlargethispage{1.5\baselineskip}
Figure~\ref{fig:db_schema} depicts the relational entity connections, state mapping layouts, and event logging structures organized across three primary architectural tiers in the Solidity smart contract.

\begin{figure}[H]
\centering
\vspace{-0.6em}
\adjustbox{max width=0.98\linewidth, max height=0.125\textheight, keepaspectratio, center}{\input{diagrams/fig1_4_prismdb_schema_connectors.tex}}
\vspace{-0.5em}
\caption{Smart contract state schemas, data structs, and relational mappings governing voters and candidates.}
\label{fig:db_schema}
\end{figure}
\vspace{-0.6em}

\noindent\textbf{1. Composite Entity Data Structures:}
\begin{itemize}
    \setlength{\itemsep}{1.0pt}
    \setlength{\parskip}{0pt}
    \setlength{\parsep}{0pt}
    \item \textbf{Voter Struct (\texttt{struct Voter}):} Encapsulates voter state: 160-bit wallet key (\texttt{address}), registration flag (\texttt{isRegistered}), single-vote atomic flag (\texttt{hasVoted}), candidate foreign key (\texttt{votedCandidateId}), and submission timestamp. An atomic boolean flag guarantees $O(1)$ double-voting prevention.
    \item \textbf{Candidate Struct (\texttt{struct Candidate}):} Stores certified candidate profiles: unique identifier (\texttt{id}), string moniker (\texttt{name}), accumulated tally (\texttt{voteCount}), registration block number, and validity assertion (\texttt{isValid}).
\end{itemize}

\vspace{0.25em}
\noindent\textbf{2. Relational Storage Mappings and Administrative Bounds:}
\begin{itemize}
    \setlength{\itemsep}{1.0pt}
    \setlength{\parskip}{0pt}
    \setlength{\parsep}{0pt}
    \item \textbf{Internal Voter Registry:} Managed via \texttt{mapping(address => Voter) public voters}, enabling constant-time key-value lookups during ballot casting while preventing external roster enumeration.
    \item \textbf{Dynamic Candidate Array:} \texttt{Candidate[] public candidates} paired with integer counter \texttt{candidatesCount} facilitates dynamic candidate listing and direct array-index vote incrementing ($N(c) \leftarrow N(c) + 1$).
    \item \textbf{Role-Based Ownership Guard:} Contract administration is pinned to \texttt{address public admin}, restricting candidate onboarding and voter address whitelisting to certified electoral officials via the \texttt{onlyAdmin} modifier.
\end{itemize}

\vspace{0.25em}
\noindent\textbf{3. Event Receipts and Off-Chain Audit Logging:}
The contract emits a standardized \texttt{VoteCast} event upon every accepted ballot, recording indexed parameters (\texttt{address indexed voter}, \texttt{uint indexed candidateId}, \texttt{uint256 blockNumber}, \texttt{bytes32 txHash}, \texttt{bytes32 blockHash}). These event logs populate bloom filter topics in the EVM receipt trie, allowing front-end Web3 clients and external auditors to monitor tally updates in real time without incurring state-read gas costs.
"""

new_text = text[:p1] + content + text[p2:]
with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Section 5.8 cleanly written!")
