import Container from "@material-ui/core/Container"
import Grid from "@material-ui/core/Grid"
import React from "react"
import {connect} from "react-redux"
import {getBookmarks} from "selectors/bookmark"
import {useStyles} from "components/Main/style"
import BookmarkCardContent from "components/CardContent/BookmarkCardContent"

export const Main = (props) => {
  const {bookmarks} = props
  const classes = useStyles()

  return (
    <main>
      <Container className={classes.cardGrid}>
        <Grid container spacing={2}>
          {bookmarks.map(bookmark => (
            <Grid item key={bookmark.pk} xs={12} sm={6} md={3}>
              <BookmarkCardContent {...bookmark}/>
            </Grid>
          ))}
        </Grid>
      </Container>
    </main>
  )
}

const mapStateToProps = (state) => ({
  bookmarks: getBookmarks(state),
})


export default connect(
  mapStateToProps,
  null,
)(Main)
