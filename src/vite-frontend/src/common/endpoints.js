const baseEndpoint = '/api/v1/';

const endpoints = {
            questionsCRUD: `${baseEndpoint}questions/`,
            questionsAnswersList: `${baseEndpoint}questions-answers/`,
            questionsNewAnswer: `${baseEndpoint}questions-new-answer/`,
            AnswerDetail: `${baseEndpoint}answers-detail/`,
            AnswerLike: `${baseEndpoint}answers-like/`,

            usersDetail: "/auth/users/me/", ///fornito da djoser
};

export { endpoints };