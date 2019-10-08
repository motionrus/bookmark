import {fromJS, List, Record} from "immutable"

const initState = Record({
  items: List([]),
})

export default function (state = initState(), action) {
  switch (action.type) {
  case "GET_ALL_BOOKMARK":
    return state.setIn(["items"], fromJS(action.data))
  case "DELETE_BOOKMARK":
    return state.updateIn(["items"], list => (
      list.filter((item) => item.get("pk") !== action.pk)
    ))
  default:
    return state
  }
}
