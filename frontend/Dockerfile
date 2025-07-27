# frontend/Dockerfile

FROM node:20 AS builder

# Установка зависимостей
WORKDIR /app
# Копируем package.json в текущую рабочую директорию /app
COPY package*.json ./
RUN npm install

# # Копируем исходный код из контекста (который ./frontend)
COPY . ./

# Собираем прод-версию React-приложения
RUN npm run build

# Используем nginx для сервинга статики
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf