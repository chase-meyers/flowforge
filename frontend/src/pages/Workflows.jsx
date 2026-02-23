import { useEffect, useState } from "react";

import { apiGet } from "../lib/api";

function Workflows() {
  const [workflows, setWorkflows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let isMounted = true;

    async function loadWorkflows() {
      try {
        const data = await apiGet("/workflows");
        if (isMounted) {
          setWorkflows(Array.isArray(data) ? data : []);
        }
      } catch (err) {
        if (isMounted) {
          setError(err instanceof Error ? err.message : "Failed to load workflows");
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    loadWorkflows();

    return () => {
      isMounted = false;
    };
  }, []);

  function handleCreateWorkflow() {
    // Placeholder action until workflow creation form is implemented.
  }

  return (
    <div>
      <h1>Workflows</h1>
      <button type="button" onClick={handleCreateWorkflow}>
        Create New Workflow
      </button>

      {loading && <p>Loading workflows...</p>}
      {error && <p>{error}</p>}

      {!loading && !error && (
        <ul>
          {workflows.map((workflow) => (
            <li key={workflow.id}>{workflow.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Workflows;
