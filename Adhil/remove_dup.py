import os

filepath = r"c:\Users\nobin\OneDrive\Documents\Projects\PROJECT_REPORTS\Adeeba\main.tex"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

dup_marker = r"""\clearpage
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

text_norm = text.replace("\r\n", "\n")
dup_norm = dup_marker.replace("\r\n", "\n")

if dup_norm in text_norm:
    updated = text_norm.replace(dup_norm, "")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated)
    print("Duplicate block removed successfully!")
else:
    print("Could not match exact duplicate string, checking via find...")
    # Find second occurrence of \section{Smart Contract State Schemas and Structs}
    p_sec1 = text.find(r"\section{Smart Contract State Schemas and Structs}")
    p_sec2 = text.find(r"\section{Smart Contract State Schemas and Structs}", p_sec1 + 10)
    p_dfd = text.find(r"\section{Level-1 Data Flow Diagram (DFD)}")
    print(f"p_sec1: {p_sec1}, p_sec2: {p_sec2}, p_dfd: {p_dfd}")
    if p_sec2 != -1 and p_dfd != -1:
        # find \clearpage before p_sec2
        p_cp = text.rfind(r"\clearpage", 0, p_sec2)
        print(f"p_cp: {p_cp}")
        updated = text[:p_cp] + text[p_dfd - len(r"\clearpage" + "\n"):]
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated)
        print("Removed duplicate slice!")
