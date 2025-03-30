import { exportData } from "../api/api";

const Export = () => {
  const handleExport = async () => {
    const blob = await exportData();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "calculations.csv";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  };

  return (
    <div className="p-4 bg-white shadow-lg rounded-2xl">
      <h2 className="text-xl font-bold mb-4">Export</h2>
      <button
        onClick={handleExport}
        className="w-full bg-green-500 text-white p-2 rounded-lg hover:bg-green-700"
      >
        Export CSV
      </button>
    </div>
  );
};

export default Export;
