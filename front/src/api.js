import axios from "axios";


export const $axios = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/',
    headers: {
        'Content-Type': 'application/json',
        Authorization: localStorage.getItem('token') ? `Bearer ${localStorage.getItem('token')}` : null
    }
})