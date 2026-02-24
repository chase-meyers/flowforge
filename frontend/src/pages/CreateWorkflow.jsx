import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { apiPost } from "../lib/api";

function CreateWorkflow() {
  const [name, setName] = useState("");
  const [triggerType, setTriggerType] = useState("manual");
  const [definition, setDefinition] = useState("");
  const navigate = useNavigate();

  async function handleSubmit(event) {
    event.preventDefault();

    const payload = {
      name,
      userId: "00000000-0000-0000-0000-000000000001",
      trigger: {
        type: triggerType,
        definition,
      },
      steps: [],
      edges: [],
    };

    await apiPost("/workflows", payload);
    navigate("/workflows");
  }

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">Name</label>
        <input
          id="name"
          type="text"
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
      </div>

      <div>
        <label htmlFor="triggerType">Trigger Type</label>
        <select
          id="triggerType"
          value={triggerType}
          onChange={(event) => setTriggerType(event.target.value)}
        >
          <option value="manual">manual</option>
          <option value="cron">cron</option>
        </select>
      </div>

      <div>
        <label htmlFor="definition">Definition</label>
        <textarea
          id="definition"
          value={definition}
          onChange={(event) => setDefinition(event.target.value)}
        />
      </div>

      <button type="submit">Create</button>
    </form>
  );
}

export default CreateWorkflow;
