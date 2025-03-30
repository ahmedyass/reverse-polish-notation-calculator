import { useEffect, useState } from "react";
import { getHistory } from "../api/api";

interface HistoryItem {
  id: number;
  expression: string;
  result: number;
  created_at: string;
}

const History = () => {
  const [history, setHistory] = useState<HistoryItem[]>([]);

  useEffect(() => {
    const fetchHistory = async () => {
      const data: HistoryItem[] = await getHistory();
      setHistory(data);
    };
    fetchHistory();
  }, []);

  return (
    <div className="p-4 bg-white shadow-lg rounded-2xl">
      <h2 className="text-xl font-bold mb-4">History</h2>
      <ul className="list-disc pl-4">
        {history.map((item) => (
          <li key={item.id} className="text-sm">
            {item.expression} = {item.result}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default History;
