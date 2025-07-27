import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';


// https://vite.dev/config/
export default defineConfig({
    plugins: [react(), tailwindcss()],
    server: { // Добавлен объект server для host
        host: true, // 👈 обязательно для docker
        port: 5173, // Vite будет слушать на этом порту, если запускать его в dev режиме
    }
})
