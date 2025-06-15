import sys
from graph.build_graph import build_graph

def main():
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    else:
        topic = input("Enter a research topic: ")

    graph = build_graph()
    result = graph.invoke({"topic": topic})

    report = result.get("report", "")
    print("\n📝 Final Report:\n")
    print(report)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
input("Press Enter to exit...")

