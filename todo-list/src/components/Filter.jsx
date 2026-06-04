function Filter(props) {
  return (
    <div className="filter">
      <input
        type="checkbox"
        id="filter"
        name="filter"
        onChange={props.onChange}
        checked={props.checked}
      />
      <label htmlFor="filter">hide completed</label>
    </div>
  );
}

export default Filter;
