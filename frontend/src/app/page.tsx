import Image from "next/image";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold mb-8">AI Quant Strategy Builder</h1>
        <p className="text-lg mb-4">
          Welcome to the AI-powered natural language quant strategy builder.
        </p>
        <p className="text-lg">
          Get started by signing up or logging in to create and test your trading strategies.
        </p>
      </div>
    </main>
  );
}
