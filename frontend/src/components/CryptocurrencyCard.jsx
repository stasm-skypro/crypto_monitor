import { Card } from "antd";

function CryptocurrencyCard(props) {
  const { currency } = props;

  return (
    <div>
      {
        <Card
          title={
            <div style={{ display: "flex", alignItems: "center", gap: "0.75rem", fontSize: "24px" }}>
              <img
                src={`https://s2.coinmarketcap.com/static/img/coins/64x64/${currency.id}.png`}
                alt={currency.name}
                style={{ width: 32, height: 32 }}
              />
              <span>{currency.name}</span>
            </div>
          }
          style={{ width: 600 }}
        >
          <p style={{ fontSize: "18px" }}>Акивность: {currency.is_active ? "Активна" : "Неактивна"}</p>
          <p style={{ fontSize: "18px" }}>Текущая цена: {currency.quote.USD.price.toFixed(2)}$</p>
          <p style={{ fontSize: "18px" }}>
            Изменение за 24 часа:{" "}
            <span style={{ color: currency.quote.USD.volume_change_24h >= 0 ? "green" : "red" }}>
              {currency.quote.USD.volume_change_24h.toFixed(2)}$
            </span>
          </p>
          <p style={{ fontSize: "18px" }}>
            Изменение за 24 часа:{" "}
            <span style={{ color: currency.quote.USD.percent_change_24h >= 0 ? "green" : "red" }}>
              {currency.quote.USD.percent_change_24h.toFixed(2)}%
            </span>
          </p>
          <p style={{ fontSize: "18px" }}>Капитализация: {currency.quote.USD.market_cap.toFixed(2)}$</p>
          <p style={{ fontSize: "18px" }}>
            Последнее обновление:{" "}
            {new Date(currency.last_updated).toLocaleString("ru-RU", {
              day: "2-digit",
              month: "long",
              year: "numeric",
              hour: "2-digit",
              minute: "2-digit",
            })}
          </p>
        </Card>
      }
    </div>
  );
}

export default CryptocurrencyCard;
