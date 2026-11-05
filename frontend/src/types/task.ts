export interface Task {
    id: number;
    title: string;
    description: string | null;
    completed: boolean;
    created_at: string;
}

export interface TaskCreate {
    title: string;
    description: string | null;
}

export interface TaskUpdate {
    title?: string | null;
    description?: string | null;
    completed?: boolean | null;
}