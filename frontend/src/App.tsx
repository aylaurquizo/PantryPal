import React from "react";
import "./App.css";

const App: React.FC = () => {
  return (
    <div className="app">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="logo">
          <img src="/path-to-logo.png" alt="PantryPal Logo" />
        </div>
        <nav>
          <ul>
            <li>🏠</li>
            <li>🔍</li>
            <li>🔖</li>
          </ul>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="main-content">
        <header className="header">
          <h1>Welcome to PantryPal</h1>
          <h2>Input your ingredients to find recipes</h2>
          <div className="search-bar">
            <input type="text" placeholder="Search for recipes" />
            <button>🔍</button>
          </div>
        </header>

        <section className="trending-recipes">
          <h2>Trending Recipes:</h2>
          <div className="recipes-grid">
            {Array.from({ length: 3 }).map((_, index) => (
              <div key={index} className="recipe-card">
                <div className="recipe-placeholder">📷</div>
                <p>Recipe Name</p>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
};

export default App;
