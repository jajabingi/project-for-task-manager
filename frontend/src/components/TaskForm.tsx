import { useState } from "react";

import type { FormEvent } from "react";

import type { TaskCreate } from "../types/task";


interface TaskFormProps {
    onCreate: (task: TaskCreate) => Promise<void>;
}


function TaskForm({ onCreate }: TaskFormProps) {

    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");

    const [loading, setLoading] = useState(false);


    const handleSubmit = async (event: FormEvent) => {

        event.preventDefault();

        if (!title.trim()) {
            return;
        }

        setLoading(true);

        try {

            await onCreate({
                title: title.trim(),
                description: description.trim() || null
            });

            setTitle("");
            setDescription("");

        } finally {

            setLoading(false);

        }
    };


    return (

        <form className="task-form" onSubmit={handleSubmit}>

            <h2>Create a task</h2>

            <input
                type="text"
                placeholder="Task title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                maxLength={255}
                required
            />

            <textarea
                placeholder="Task description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />

            <button type="submit" disabled={loading}>
                {loading ? "Creating..." : "Add task"}
            </button>

        </form>

    );
}


export default TaskForm;