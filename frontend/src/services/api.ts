import axios from "axios";

import type {
    Task,
    TaskCreate,
    TaskUpdate
} from "../types/task";


const api = axios.create({
    baseURL: "/api",
    headers: {
        "Content-Type": "application/json"
    }
});


export const getTasks = async (): Promise<Task[]> => {

    const response = await api.get<Task[]>("/tasks/");

    return response.data;
};


export const createTask = async (
    task: TaskCreate
): Promise<Task> => {

    const response = await api.post<Task>(
        "/tasks/",
        task
    );

    return response.data;
};


export const updateTask = async (
    id: number,
    task: TaskUpdate
): Promise<Task> => {

    const response = await api.patch<Task>(
        `/tasks/${id}`,
        task
    );

    return response.data;
};


export const deleteTask = async (
    id: number
): Promise<void> => {

    await api.delete(`/tasks/${id}`);
};