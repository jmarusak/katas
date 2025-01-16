import './SearchBar.css';

const SearchBar = ({ onSubmit }) => {
  const handleFormSubmit = (event) => {
    event.preventDefault();
    
    const term = event.target.elements[0].value;
    onSubmit(term);
  }

  return (
    <div className="search-bar">
      <form onSubmit={handleFormSubmit}>
        <label>Enter Search Term</label>
        <input />
      </form>
    </div>
  ); 
}

export default SearchBar;
