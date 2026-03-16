import random
from pathlib import Path


class JBVPAgent:
    def __init__(self, data_dir: str = "data") -> None:
        self.data_dir = Path(data_dir)
        self.knowledge_base = self._load_knowledge()

    def _load_knowledge(self) -> dict[str, str]:
        kb = {
            "pharmacology unit 2": (
                "Unit 2 focuses on ADME: drug absorption, distribution, metabolism, and excretion. "
                "It also covers bioavailability, first-pass metabolism, enzyme induction/inhibition, "
                "and factors affecting plasma concentration."
            ),
            "admission": (
                "Admissions are generally based on eligibility criteria, merit lists, "
                "and counseling rounds published by the college."
            ),
            "syllabus": "Syllabus details are organized by semester and subject credits.",
            "events": "College events include orientation, seminars, practical workshops, and annual fest.",
        }

        if self.data_dir.exists():
            for txt_file in self.data_dir.glob("*.txt"):
                kb[txt_file.stem.lower()] = txt_file.read_text(encoding="utf-8")
        return kb

    def chat(self, query: str) -> str:
        q = query.lower().strip()
        for key, value in self.knowledge_base.items():
            if key in q:
                return value

        return (
            "I can help with B.Pharm notes, assignment help, viva prep, "
            "college information, and random question paper generation. "
            "Please ask a specific topic."
        )

    def summarize(self, text: str) -> str:
        sentences = [s.strip() for s in text.split(".") if s.strip()]
        if not sentences:
            return "Please provide text to summarize."
        return ". ".join(sentences[:2]) + "."

    def assignment_help(self, topic: str, mode: str) -> str:
        normalized_mode = mode.lower().strip()
        if normalized_mode == "viva_questions":
            return (
                f"Viva questions for {topic}:\n"
                "1) Define the topic in one line.\n"
                "2) Explain mechanism/action with one example.\n"
                "3) Mention one clinical or practical application."
            )

        return (
            f"Assignment help for {topic}:\n"
            "- Introduction\n"
            "- Core concepts\n"
            "- Applications\n"
            "- Conclusion"
        )

    def college_info(self, query: str) -> str:
        return self.chat(query)

    def generate_question_paper(self, subject: str, total_questions: int) -> list[str]:
        templates = [
            "Define {subject} and explain its scope.",
            "Write a short note on key principles of {subject}.",
            "Explain the practical applications of {subject}.",
            "Differentiate between two major concepts in {subject}.",
            "Discuss challenges and future trends in {subject}.",
        ]

        questions = []
        for idx in range(total_questions):
            template = random.choice(templates)
            questions.append(f"Q{idx + 1}. " + template.format(subject=subject))
        return questions
