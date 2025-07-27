import { BarsOutlined } from "@ant-design/icons";
import { Menu, Spin } from "antd";
import axios from "axios";
import { useEffect, useState } from "react";
import CryptocurrencyCard from "./components/CryptocurrencyCard.jsx";

// Вспомогательная функция
function getItem(label, key, icon, children, type) {
  return {
    label,
    key,
    icon,
    children,
    type,
  };
}

const App = () => {
  const [currencies, setCurrencies] = useState([]);
  const [currencyID, setCurrencyID] = useState(1);
  const [currencyData, setCurrencyData] = useState(null);

  // Получение списка криптовалют
  const fetchCurrencies = async () => {
    try {
      // const response = await axios.get("http://127.0.0.1:8000/currencies");
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/currencies`);
      const currenciesData = response.data;

      const menuItems = [
        getItem("Меню криптовалют", "sub1", <BarsOutlined />, [
          getItem(
            null,
            "g1",
            null,
            currenciesData.map((c) => ({
              label: c.name,
              key: c.id,
            })),
            "group",
          ),
        ]),
      ];

      setCurrencies(menuItems);
    } catch (error) {
      console.error("Ошибка при получении валют:", error);
    }
  };

  // Получение информации о выбранной криптовалюте
  const fetchCurrency = async () => {
    try {
      // const response = await axios.get(`http://127.0.0.1:8000/currencies/${currencyID}`);
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/currencies/${currencyID}`);
      const currencyData = response.data;

      setCurrencyData(currencyData);
    } catch (error) {
      console.error("Ошибка при получении информации о криптовалюте:", error);
    }
  };

  useEffect(() => {
    fetchCurrencies();
  }, []);

  useEffect(() => {
    setCurrencyData(null);
    fetchCurrency();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currencyID]);

  const onClick = (e) => {
    setCurrencyID(e.key);
    
    // console.log("click ", e);
  };

  return (
    <div className="flex">
      <Menu
        onClick={onClick}
        style={{ width: 256 }}
        defaultSelectedKeys={["1"]}
        defaultOpenKeys={["sub1"]}
        mode="inline"
        items={currencies}
        theme="dark"
        className="h-screen overflow-scroll"
      />
      <div className="mx-auto my-auto">
        {currencyData ? <CryptocurrencyCard currency={currencyData} /> : <Spin size="large" />}
      </div>
    </div>
  );
};

export default App;
