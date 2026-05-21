import { useState } from 'react';
import axios from 'axios';

function App() {

  const [news, setNews] = useState('');
  const [result, setResult] = useState('');

  const checkCredibility = async () => {

    // Prevent empty input
    if (!news.trim()) {
      setResult("Please enter news text");
      return;
    }

    try {

      const response = await axios.post(
        'https://fake-news-detection-credibility-scoring.onrender.com/predict',
        {
          text: news
        }
      );

      setResult(response.data?.prediction || "No result from server");

    } catch (error) {

      console.log(error);
      setResult("Server Error");

    }
  };

  return (

    <div style={{
      padding: '40px',
      fontFamily: 'Arial',
      textAlign: 'center'
    }}>

      <h1>Fake News Detection and Credibility Scoring Platform</h1>

      <textarea
        rows="10"
        cols="70"
        placeholder="Enter news content here..."
        value={news}
        onChange={(e) => setNews(e.target.value)}
      />

      <br /><br />

      <button onClick={checkCredibility}>
        Check Credibility
      </button>

      <h2>{result}</h2>

    </div>
  );
}

export default App;