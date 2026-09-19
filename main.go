package main
import ("encoding/json"; "net/http"; "os")
func main() {
    port := os.Getenv("PORT"); if port == "" { port = os.Getenv("APP_PORT") }; if port == "" { port = "8080" }
    version, branch := "v2", "go-v2"
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        if r.URL.Path == "/" || r.URL.Path == "/health" {
            w.Header().Set("Content-Type", "application/json"); w.WriteHeader(200)
            json.NewEncoder(w).Encode(map[string]string{"status":"ok","runtime":"go","source":"github","version":version,"branch":branch}); return
        }
        w.WriteHeader(404)
    })
    http.ListenAndServe("0.0.0.0:"+port, nil)
}
