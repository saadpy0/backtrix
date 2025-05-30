import Image from "next/image";

export default function Home() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-lg font-medium text-gray-900 mb-4">Welcome to AI Quant Strategy Builder</h2>
        <p className="text-gray-600">
          Upload your data or enter a stock ticker to get started with building and backtesting trading strategies.
        </p>
      </div>
    </div>
  );
}
