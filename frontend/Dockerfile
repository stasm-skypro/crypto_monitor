# frontend/Dockerfile

FROM node:20-alpine

# Установка зависимостей
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install

# Копируем исходный код
COPY frontend .

# Собираем прод-версию React-приложения
RUN npm run build

# Используем nginx для сервинга статики
FROM nginx:stable-alpine
COPY --from=0 /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]