export const API_BASE_URL = "http://localhost:8000/api";

export interface CalculationResponse {
  id: number;
  expression: string;
  result: number;
  created_at: string;
}

export interface APIError {
  detail: string;
}

export const calculateExpression = async (
  expression: string
): Promise<CalculationResponse> => {
  try {
    const response = await fetch(`${API_BASE_URL}/calculate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ expression }),
    });

    if (!response.ok) {
      const errorData: APIError = await response.json();
      throw new Error(errorData.detail || "Failed to calculate expression");
    }

    return response.json();
  } catch (error) {
    throw new Error((error as Error).message || "Unexpected error");
  }
};

export const getHistory = async (): Promise<CalculationResponse[]> => {
  try {
    const response = await fetch(`${API_BASE_URL}/history`);

    if (!response.ok) {
      throw new Error("Failed to fetch history");
    }

    return response.json();
  } catch (error) {
    throw new Error((error as Error).message || "Unexpected error");
  }
};

export const exportData = async (): Promise<Blob> => {
  try {
    const response = await fetch(`${API_BASE_URL}/export`);

    if (!response.ok) {
      throw new Error("Failed to export data");
    }

    return response.blob();
  } catch (error) {
    throw new Error((error as Error).message || "Erreur inattendue");
  }
};
