const express = require('express');
const { exec } = require('child_process');

const app = express();
const port = 3000;

app.get('/', (request, response) => {
    exec('open .', (error, stdout, stderr) => {
        if (error) {
          console.error(`error: ${error.message}`);
          return;
        }
        if (stderr) {
          console.error(`stderr: ${stderr}`);
          return;
        }
      
        console.log(`stdout:\n${stdout}`);
      });
      response.end('File explorer open sucessful')
});

app.listen(port,() => {
    console.log(`The express server running on ${port}`);
});