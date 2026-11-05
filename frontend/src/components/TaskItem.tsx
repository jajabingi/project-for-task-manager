import type { Task } from "../types/task";


interface TaskItemProps {

    task: Task;

    onToggle: (task: Task) => Promise<void>;

    onDelete: (id: number) => Promise<void>;

}


function TaskItem({
    task,
    onToggle,
    onDelete
}: TaskItemProps) {


    return (

        <div className={`task-item ${task.completed ? "completed" : ""}`}>

            <div className="task-content">

                <h3>{task.title}</h3>

                <p>{task.description || "No description"}</p>

                <small>
                    {new Date(task.created_at).toLocaleString()}
                </small>

            </div>


            <div className="task-actions">

                <button
                    onClick={() => onToggle(task)}
                >
                    {task.completed ? "Undo" : "Complete"}
                </button>

                <button
                    className="delete-button"
                    onClick={() => onDelete(task.id)}
                >
                    Delete
                </button>

            </div>

        </div>

    );

}


export default TaskItem;