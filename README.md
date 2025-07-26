# LangChain Learning Project

A comprehensive project exploring various components and capabilities of LangChain framework.

## 🛠️ Key Components

1. **Chains**: Implementations of various LangChain chains including:
   - Sequential Chains
   - Parallel Chains
   - Conditional Chains
   - Simple Chains

2. **Document Loaders**: Support for multiple document types:
   - PDF Documents
   - CSV Files
   - Text Files
   - Web Content
   - Directory Loading

3. **Models Integration**:
   - LLM Models
   - Chat Models
   - Embedding Models
   - Document Similarity

4. **Output Processing**:
   - JSON Output Parsing
   - Pydantic Output Parsing
   - String Output Parsing
   - Structured Output Parsing

5. **Vector Store & RAG**:
   - Chroma Vector Store
   - Retrievers
   - Simple RAG Implementation

## 🚀 Getting Started

1. Clone the repository
2. Create a `.env` file with required API keys:
   ```
   GOOGLE_API_KEY=""
   HUGGINGFACEHUB_ACCESS_TOKEN=""
   EXCHANGERATE_API_KEY=""
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📚 Examples

Each directory contains practical examples and implementations. Notable examples include:
- Currency conversion using tools
- Simple chatbot implementations
- Document similarity analysis
- RAG (Retrieval Augmented Generation) implementations

## 🔧 Technologies Used

- LangChain
- Google Generative AI
- Hugging Face
- ChromaDB
- Various LLM Models
