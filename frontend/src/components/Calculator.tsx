import { useState } from "react";
import { calculateExpression } from "../api/api";

const Calculator = () => {
  const [expression, setExpression] = useState("");
  const [result, setResult] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleCalculate = async () => {
    if (!expression.trim()) {
      setError("Saisissez une expression correct svp.");
      return;
    }

    setError(null);
    setResult(null);

    try {
      const data = await calculateExpression(expression);
      setResult(data.result.toString());
    } catch (err) {
      setError((err as Error).message);
    }
  };

  return (
    <div className="p-4 bg-white shadow-lg rounded-2xl">
      <h2 className="text-xl font-bold mb-4">Calculator</h2>
      <input
        type="text"
        placeholder="Enter RPN Expression"
        value={expression}
        onChange={(e) => setExpression(e.target.value)}
        className="w-full p-2 border rounded-lg"
      />
      <button
        onClick={handleCalculate}
        className="mt-2 w-full bg-blue-500 text-white p-2 rounded-lg hover:bg-blue-700"
      >
        Calculer
      </button>

      {result !== null && (
        <p className="mt-2 text-lg font-semibold text-green-600">
          Resultat: {result}
        </p>
      )}

      {error && (
        <p className="mt-2 text-sm text-red-600 bg-red-100 p-2 rounded-lg">
          {error}
        </p>
      )}
    </div>
  );
};

export default Calculator;
