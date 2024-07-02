function formatDate(date) {
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    
    const day = date.getDate();
    const month = months[date.getMonth()];
    const year = date.getFullYear();

    return `${month} ${day < 10 ? '0' : ''}${day}, ${year}`;
}

const today = new Date();
const formattedDate = formatDate(today);
document.querySelector('#date').innerHTML = formattedDate;
console.log(formattedDate);  // e.g., "Jun 22, 2024"
