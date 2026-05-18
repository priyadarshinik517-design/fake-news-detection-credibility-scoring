import { useState } from 'react';
import axios from 'axios';

function App() {

  const [news, setNews] = useState('');
  const [result, setResult] = useState('');

  const checkCredibility = async () => {

    // ✅ prevent empty input
    if (!news.trim()) {
      setResult("Please enter news text");
      return;
    }

    try {

      const response = await axios.post(
        'http://127.0.0.1:5000/predict',
        {
          text: news
        }
      );

      // ✅ safe check
      setResult(response.data?.prediction || "No result from server");

    } catch (error) {

      console.log(error);
      setResult("Server Error (Check backend running)");

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