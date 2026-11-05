import type { Task } from "../types/task";

import TaskItem from "./TaskItem";


interface TaskListProps {

    tasks: Task[];

    onToggle: (task: Task) => Promise<void>;

    onDelete: (id: number) => Promise<void>;

}


function TaskList({
    tasks,
    onToggle,
    onDelete
}: TaskListProps) {


    if (tasks.length === 0) {

        return (

            <div className="empty-state">
                <h3>No tasks yet</h3>
                <p>Create your first task above.</p>
            </div>

        );

    }


    return (

        <div className="task-list">

            {tasks.map((task) => (

                <TaskItem
                    key={task.id}
                    task={task}
                    onToggle={onToggle}
                    onDelete={onDelete}
                />

            ))}

        </div>

    );

}


export default TaskList;