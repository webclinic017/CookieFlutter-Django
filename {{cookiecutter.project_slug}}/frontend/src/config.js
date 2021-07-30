const url = document.location.toString().toLowerCase();
const path = url.split('//')[1];
const domain = path.split('/')[0];
const config = {
    API_URL: `$https://${domain}/api`,
};

// const config = {
//     API_URL: process.env.REACT_APP_API_URL,
// };

export default config;
