FROM golang
ADD kongExample /go/src/github.com/narenaryan/kongExample
WORKDIR /go/src/github.com/narenaryan/kongExample
RUN go get github.com/gorilla/mux
RUN go install github.com/svtter/kongExample
ENTRYPOINT /go/bin/kongExample