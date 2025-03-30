import Calculator from "../components/Calculator";
import Export from "../components/Export";
import History from "../components/History";

const Home = () => {
  return (
    <div className="min-h-screen flex flex-col items-center bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-6">Calculatrice en Notation Polonaise Inverse (NPI)</h1>
      <div className="flex flex-col gap-6 w-full max-w-4xl">
        <Calculator />
        <Export />
        <History />
      </div>
    </div>
  );
};

export default Home;
