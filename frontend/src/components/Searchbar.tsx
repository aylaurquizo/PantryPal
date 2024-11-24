import React, { useState } from "react";

const Searchbar: React.FC = () => {
  const [ingredient, setIngredient] = useState<string>(""); // State for search input
  const [loading, setLoading] = useState<boolean>(false); // State for loading indicator
  const [message, setMessage] = useState<string | null>(null); // Feedback message

  // Function to handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    // Replace with the actual user ID (can be dynamic)
    const user_id = 1;

    try {
      const response = await fetch("/add_ingredient", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id,
          ingredient_name: ingredient,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        setMessage(data.message); // Show success message
      } else {
        const errorData = await response.json();
        setMessage(errorData.error || "An error occurred.");
      }
    } catch (error) {
      console.error("Error adding ingredient:", error);
      setMessage("An unexpected error occurred.");
    } finally {
      setLoading(false);
      setIngredient(""); // Clear input
    }
  };

  return (
    <div className="searchbar-container">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter an ingredient"
          value={ingredient}
          onChange={(e) => setIngredient(e.target.value)}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? "Adding..." : "Add"}
        </button>
      </form>
      {message && <p className="feedback-message">{message}</p>}
    </div>
  );
};

export default Searchbar;