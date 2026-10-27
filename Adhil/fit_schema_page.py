import os

filepath = r"c:\Users\nobin\OneDrive\Documents\Projects\PROJECT_REPORTS\Adeeba\main.tex"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

start_kw = r"\section{Block Structure and Cryptographic Chaining}"
end_kw = r"\clearpage"

p1 = text.find(start_kw)
p2 = text.find(end_kw, p1)

if p1 == -1 or p2 == -1:
    print(f"Error finding markers: p1={p1}, p2={p2}")
    exit(1)

content = r"""\section{Block Structure and Cryptographic Chaining}
Figure~\ref{fig:block_structure} details the internal architecture of blocks within the blockchain ledger, demonstrating how block headers, cryptographic timestamps $T_i$, nonces $n_i$, and transaction sets $Tx_i$ are chained via SHA-256 hashing.

\begin{figure}[H]
\centering
\adjustbox{max width=0.98\linewidth, max height=0.55\textheight, keepaspectratio, center}{\input{diagrams/dag_task_graph_scheduling.tex}}
\caption{Cryptographic block structure and hash chaining mechanism illustrating ledger immutability.}
\label{fig:block_structure}
\end{figure}

The cryptographic linking between consecutive blocks $B_{i-1}$ and $B_i$ guarantees that historical records cannot be retroactively modified without invalidating all downstream block hashes. Each block encapsulates the Merkle root summarizing its transaction set $Tx_i$, ensuring that any attempted alteration of a single cast vote invalidates the entire block header digest.

\clearpage
\section{Smart Contract State Schemas and Structs}
\enlargethispage{\baselineskip}
Figure~\ref{fig:db_schema} depicts the relational entity connections and state mapping layouts maintained in the Solidity smart contract.

\begin{figure}[H]
\centering
\vspace{-0.5em}
\adjustbox{max width=0.98\linewidth, max height=0.20\textheight, keepaspectratio, center}{\input{diagrams/fig1_4_prismdb_schema_connectors.tex}}
\vspace{-0.6em}
\caption{Smart contract state schemas, data structs, and relational mappings governing voters and candidates.}
\label{fig:db_schema}
\end{figure}
\vspace{-0.5em}

The smart contract architectural schema organizes state storage, relational entity bindings, and cryptographic proof generation across three primary tiers:

\vspace{0.25em}
\noindent\textbf{1. Composite Entity Data Structures:}
\begin{itemize}
    \setlength{\itemsep}{1.2pt}
    \setlength{\parskip}{0pt}
    \setlength{\parsep}{0pt}
    \item \textbf{Voter Struct (\texttt{struct Voter}):} Encapsulates voter state, including the 160-bit Ethereum wallet key (\texttt{address}), registration authorization (\texttt{isRegistered}), single-vote enforcement flag (\texttt{hasVoted}), candidate choice foreign key (\texttt{votedCandidateId}), and chronological participation timestamp (\texttt{voteTimestamp}). Enforcing \texttt{hasVoted} as an atomic boolean flag guarantees $O(1)$ constant-time double-voting prevention.
    \item \textbf{Candidate Struct (\texttt{struct Candidate}):} Stores certified candidate profiles, containing candidate numerical identifier (\texttt{id}), string moniker (\texttt{name}), real-time accumulated vote tally (\texttt{voteCount}), block number of administrative registration (\texttt{registrationBlock}), and eligibility flag (\texttt{isValid}).
\end{itemize}

\vspace{0.25em}
\noindent\textbf{2. Relational Storage Mappings and Administrative Bounds:}
\begin{itemize}
    \setlength{\itemsep}{1.2pt}
    \setlength{\parskip}{0pt}
    \setlength{\parsep}{0pt}
    \item \textbf{Internal Voter Registry:} Implemented via \texttt{mapping(address => Voter) public voters}, enabling constant-time key-value lookups during ballot casting while preventing external enumeration of the complete voter roll.
    \item \textbf{Dynamic Candidate Array:} \texttt{Candidate[] public candidates} along with integer counter \texttt{candidatesCount} facilitates dynamic candidate listing and direct array-index vote incrementing ($N(c) \leftarrow N(c) + 1$).
    \item \textbf{Role-Based Ownership Guard:} Contract administration is pinned to \texttt{address public admin}, restricting candidate onboarding and voter address whitelisting to certified electoral officials via the \texttt{onlyAdmin} modifier.
\end{itemize}

\vspace{0.25em}
\noindent\textbf{3. Event Receipts and Off-Chain Audit Logging:}
The contract emits a standardized \texttt{VoteCast} event upon every accepted ballot, recording indexed parameters (\texttt{address indexed voter}, \texttt{uint indexed candidateId}, \texttt{uint256 blockNumber}, \texttt{bytes32 txHash}, \texttt{bytes32 blockHash}). These event logs populate bloom filter topics in the EVM receipt trie, allowing front-end Web3 clients and external auditors to monitor tally updates in real time without incurring state-read gas costs.
"""

new_text = text[:p1] + content + text[p2:]
with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Compact, complete Section 5.8 updated successfully!")
