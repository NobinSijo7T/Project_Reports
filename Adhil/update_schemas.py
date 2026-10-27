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
Figure~\ref{fig:db_schema} depicts the relational entity connections and state mapping layouts maintained in the Solidity smart contract.

\begin{figure}[H]
\centering
\vspace{-0.4em}
\adjustbox{max width=0.98\linewidth, max height=0.26\textheight, keepaspectratio, center}{\input{diagrams/fig1_4_prismdb_schema_connectors.tex}}
\vspace{-0.5em}
\caption{Smart contract state schemas, data structs, and relational mappings governing voters and candidates.}
\label{fig:db_schema}
\end{figure}
\vspace{-0.4em}

The smart contract architectural schema organizes state storage, relational bindings, and cryptographic proof generation across three key layers:

\vspace{0.25em}
\noindent\textbf{Entity Struct Definitions:}
\begin{itemize}
    \setlength{\itemsep}{1.0pt}
    \setlength{\parskip}{0pt}
    \setlength{\parsep}{0pt}
    \item \textbf{Voter Struct (\texttt{struct Voter}):} Encapsulates voter identity and eligibility attributes, including the 160-bit hexadecimal Ethereum wallet address (\texttt{address}), registration authorization flag (\texttt{isRegistered}), single-vote enforcement flag (\texttt{hasVoted}), the selected candidate identifier (\texttt{votedCandidateId}), and the block timestamp of ballot submission (\texttt{voteTimestamp}). Enforcing \texttt{hasVoted} as an atomic boolean flag within the struct ensures $O(1)$ state verification.
    \item \textbf{Candidate Struct (\texttt{struct Candidate}):} Encapsulates certified ballot options, including the candidate numerical identifier (\texttt{id}), display moniker string (\texttt{name}), accumulated vote tally (\texttt{voteCount}), block number of administrative registration (\texttt{registrationBlock}), and an active status flag (\texttt{isValid}).
\end{itemize}

\vspace{0.25em}
\noindent\textbf{Relational Storage Mappings and Administrative Bounds:}
\begin{itemize}
    \setlength{\itemsep}{1.0pt}
    \setlength{\parskip}{0pt}
    \setlength{\parsep}{0pt}
    \item \textbf{Voter Registry Mapping:} The smart contract maintains persistent EVM storage mappings linking cryptographic voter addresses to individual records via \texttt{mapping(address => Voter) public voters}. This key-value organization prevents unauthorized enumeration of citizen rosters while guaranteeing constant-time lookup during transaction validation.
    \item \textbf{Candidate Array and Counters:} An ordered dynamic array \texttt{Candidate[] public candidates} paired with integer counter \texttt{candidatesCount} preserves candidate indexes and allows constant-time tally increments when a ballot is accepted.
    \item \textbf{Access Control Ownership:} Administrative authority is anchored to \texttt{address public admin}, restricting candidate registration and voter whitelisting to certified electoral authorities through the \texttt{onlyAdmin} function modifier.
\end{itemize}

\vspace{0.25em}
\noindent\textbf{Event Receipts and Immutable Logging:}
The contract emits a standardized \texttt{VoteCast} event upon each successful ballot submission, recording indexed parameters (\texttt{address indexed voter}, \texttt{uint indexed candidateId}, \texttt{uint256 blockNumber}, \texttt{bytes32 txHash}). These logs generate bloom filter topics that allow off-chain Web3 front-ends and public audit monitors to verify ballot inclusion and update real-time visual dashboards without incurring state-read gas charges.
"""

new_text = text[:p1] + content + text[p2:]
with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Updated Section 5.7 and Section 5.8 successfully!")
