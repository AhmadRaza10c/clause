from app.services.chat import RAGService

def main()-> None:
    rag_services = RAGService()
    try:
        query = input("You: ").strip()
        result = rag_services.ask(query)
        print(f"AI: {result.answer}")
        if result.sources:
            print("sources: ")
            for s in result.sources:
                print(f"-- {s.source}, page: {s.page}, source: {s.score}")
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        rag_services.close()


if __name__ == "__main__":
    main()
