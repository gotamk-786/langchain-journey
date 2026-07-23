# ============================================
# REAL PROJECT 1: MOVIE INFORMATION EXTRACTOR
# Chat Prompt + Structured Output + Loop
# ============================================

from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# ─── Structure ───
class MovieInfo(BaseModel):
    movie_name:    str
    year:          int
    director:      str
    cast:          str
    genre:         str
    imdb_rating:   float
    awards:        str
    quick_summary: str
    why_watch:     str

# ─── Model ───
model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
structured_model = model.with_structured_output(MovieInfo)

# ─── Template ───
template = ChatPromptTemplate.from_messages([
    ("system", """You are an expert movie information extractor.
     Extract all details from the paragraph.
     If something is not mentioned, write: Not mentioned"""),
    ("human", "Extract information from this paragraph:\n\n{paragraph}")
])

# ─── 3 Movies ───
movies = [
    """The Dark Knight, released in 2008, is a superhero crime thriller directed by Christopher
    Nolan and produced by Warner Bros. The film features Christian Bale as Batman alongside
    Heath Ledger, Aaron Eckhart, and Gary Oldman. The plot focuses on Batman's battle against
    the chaotic criminal mastermind known as the Joker, whose actions plunge Gotham City
    into anarchy. Heath Ledger's performance earned widespread acclaim and a posthumous
    Academy Award. The film currently holds an IMDb rating of 9.0 and is praised for its
    intense storytelling and grounded realism.""",

    """3 Idiots is a 2009 Indian coming-of-age comedy-drama directed by Rajkumar Hirani.
    The film stars Aamir Khan, R. Madhavan, Sharman Joshi, Kareena Kapoor, and Boman Irani.
    Set in an engineering college, the story explores themes of friendship, academic pressure,
    and following one's passion rather than societal expectations. The movie became one of the
    highest-grossing Indian films of its time. It has a rating of 8.4 on IMDb.""",

    """Interstellar is a visually stunning science fiction epic directed by Christopher Nolan.
    Released in 2014, the film stars Matthew McConaughey, Anne Hathaway, Jessica Chastain,
    and Michael Caine. The story revolves around astronauts who travel through a wormhole
    near Saturn. The movie was widely appreciated for its emotional depth, scientific accuracy,
    and Hans Zimmer's powerful soundtrack. It holds a rating of 8.6 on IMDb."""
]

# ─── Run ───
for i, paragraph in enumerate(movies, 1):
    print(f"\n{'='*55}")
    print(f"  MOVIE {i}")
    print('='*55)

    prompt = template.invoke({"paragraph": paragraph})
    result = structured_model.invoke(prompt)

    print(f"Movie Name  : {result.movie_name}")
    print(f"Year        : {result.year}")
    print(f"Director    : {result.director}")
    print(f"Cast        : {result.cast}")
    print(f"Genre       : {result.genre}")
    print(f"IMDb Rating : {result.imdb_rating}")
    print(f"Awards      : {result.awards}")
    print(f"Summary     : {result.quick_summary}")
    print(f"Why Watch   : {result.why_watch}")
